"""★ FILE ĐỘI SỬA (1/3): cổng cấp hệ thống, nằm NGOÀI model và prompt.

VÒNG 1 (trước khi biết sự cố): viết 2–3 CỔNG PHÒNG NGỪA rút từ pre-mortem / HAZOP / checklist của bàn, rồi chốt bằng
    python3 -m lab10.checkpoint        (chép file này thành guards_round1.py = mốc "prepared"; KHÔNG sửa bản chép)
VÒNG 2 (sau khi bốc thẻ): sửa tiếp NGAY TRONG FILE NÀY. Giữ các cổng vòng 1, thêm cổng mới.
Hai file còn lại bàn được sửa: lab10/monitors.py (chỉ số theo dõi) và config/operating_gates.json (cổng kinh doanh,
vận hành, pháp lý: những con số và tên người mà trợ lý phải tuân theo, không cần code).

Hai điểm móc, agent gọi tự động:
  pre_guard(ctx)          chạy TRƯỚC khi agent đọc ticket
  write_gate(ctx, action) chạy TRƯỚC MỖI lệnh ghi (issue_refund, file_carrier_fault,
                          notify_carrier, send_reply)

Trả về một Verdict:
  Verdict.allow()                       cho qua   (pre_guard: allow(policy_id="...") để ghim phiên bản chính sách)
  Verdict.deny("lý do")                 bỏ riêng lệnh ghi này, agent đi tiếp
  Verdict.escalate("lý do")             dừng, chuyển ticket cho người
  Verdict.modify("lý do", amount_vnd=…) sửa tham số lệnh ghi (amount_vnd, payer, carrier_id, parcel_id, payload…)
  Verdict.rewrite("lý do", text)        chỉ pre_guard: thay nội dung ticket mà agent sẽ đọc

ctx.ticket   ticket gốc (chữ khách viết là DỮ LIỆU, không phải lệnh)
ctx.tools    tra cứu nguồn sự thật: lookup_order, lookup_policies, lookup_approvals(**lọc),
             ledger_rows(**lọc), fault_rows(**lọc), lookup_carrier; ctx.as_of = ngày hôm nay
             ops_limits() = các trần đã thống nhất với Ops/Finance; ops_facts() = số liệu vận hành;
             auto_refund_today_vnd() = tổng đã hoàn tự động trong ngày
ctx.gates    config cổng của bàn (config/operating_gates.json), chỉ đọc;  ctx.cost_vnd = tiền LLM đã tốn cho ticket này
ctx.events   trace tới thời điểm này;  ctx.log("ten_su_kien", ...) ghi thêm sự kiện guard vào trace
lab10.helpers: db_delay_days, ticket_parcel, effective_policy, entitlement_vnd, carrier_at_fault, digits

Mặc định dưới đây cho qua tất cả (= mốc base).
"""
from . import helpers as H  # noqa: F401
from .tools import Verdict


def _contains_recipient_pii(value, pii_values):
    """Detect exact recipient identifiers embedded in outbound strings/containers."""
    if isinstance(value, dict):
        return any(_contains_recipient_pii(v, pii_values) for v in value.values())
    if isinstance(value, (list, tuple)):
        return any(_contains_recipient_pii(v, pii_values) for v in value)
    if not isinstance(value, str):
        return False
    text = value.casefold()
    digits = H.digits(value)
    for raw in pii_values:
        if not isinstance(raw, str) or not raw.strip():
            continue
        candidate = raw.strip()
        if len(candidate) >= 5 and candidate.casefold() in text:
            return True
        number = H.digits(candidate)
        if len(number) >= 7 and number in digits:
            return True
    return False


def pre_guard(ctx):
    return Verdict.allow()


def write_gate(ctx, action):
    # action = {"tool": "issue_refund", "ticket_id":..., "order_id":..., "amount_vnd":..., "payer":..., ...}
    tool = action.get("tool")
    order_id = action.get("order_id")

    # Do not let a customer-provided delay override tracking before an irreversible write.
    if tool in ("issue_refund", "file_carrier_fault"):
        order = ctx.tools.lookup_order(order_id) if order_id else None
        if order is None:
            ctx.log("guard_missing_order", tool=tool, order_id=order_id)
            return Verdict.escalate("không tra được đơn hàng nguồn để xác minh trước khi ghi")
        try:
            parcel = H.ticket_parcel(order, ctx.ticket, ctx.as_of or ctx.tools.as_of)
            db_delay = H.db_delay_days(parcel, ctx.as_of or ctx.tools.as_of)
        except (KeyError, TypeError, ValueError):
            ctx.log("guard_incomplete_tracking", tool=tool, order_id=order_id)
            return Verdict.escalate("dữ liệu tracking thiếu hoặc không hợp lệ; cần người xác minh")

        proposed_delay = action.get("delay_days")
        if proposed_delay is None:
            proposed_delay = next((e.get("delay_days_used") for e in reversed(ctx.events)
                                   if e.get("type") == "proposal"), None)
        if proposed_delay is not None and proposed_delay != db_delay:
            ctx.log("guard_tracking_delay_mismatch", tool=tool, order_id=order_id,
                    tracking_delay_days=db_delay, proposed_delay_days=proposed_delay)
            return Verdict.escalate("số ngày trễ trong quyết định không khớp tracking; cần người duyệt")

    # A carrier fault must be tied to the recorded parcel, carrier and an allowed cause.
    if tool == "file_carrier_fault":
        order = ctx.tools.lookup_order(order_id)
        parcel = next((p for p in order.get("parcels", [])
                       if p.get("parcel_id") == action.get("parcel_id")), None)
        policies = ctx.tools.lookup_policies()
        policy = H.effective_policy(policies, ctx.as_of or ctx.tools.as_of)
        if parcel is None or policy is None:
            ctx.log("guard_unverified_carrier_fault", order_id=order_id,
                    parcel_id=action.get("parcel_id"))
            return Verdict.deny("không xác minh được kiện hoặc chính sách hiệu lực để ghi lỗi hãng")
        if (action.get("carrier_id") != parcel.get("carrier_id") or
                parcel.get("delay_cause") not in policy.get("fault_causes", [])):
            ctx.log("guard_unverified_carrier_fault", order_id=order_id,
                    parcel_id=action.get("parcel_id"), recorded_cause=parcel.get("delay_cause"))
            return Verdict.deny("tracking không xác nhận hãng và nguyên nhân đủ điều kiện ghi lỗi")

    # Limit outbound carrier notices to fields approved by the effective policy.
    if tool == "notify_carrier":
        policies = ctx.tools.lookup_policies()
        policy = H.effective_policy(policies, ctx.as_of or ctx.tools.as_of)
        if policy is None:
            return Verdict.deny("không xác định được chính sách hiệu lực cho thông báo hãng")
        allowed = set(policy.get("carrier_notice_fields", []))
        payload = action.get("payload") or {}
        safe_payload = {key: value for key, value in payload.items() if key in allowed}
        order = ctx.tools.lookup_order(order_id) if order_id else None
        recipient = (order or {}).get("recipient") or {}
        pii_values = [recipient.get(key) for key in ("name", "phone", "street", "city")]
        value_pii_fields = sorted(key for key, value in safe_payload.items()
                                  if _contains_recipient_pii(value, pii_values))
        for key in value_pii_fields:
            safe_payload.pop(key, None)

        if safe_payload != payload:
            removed = sorted(set(payload) - set(safe_payload))
            ctx.log("guard_carrier_notice_fields_removed", removed_fields=removed,
                    recipient_pii_value_fields=value_pii_fields)
            return Verdict.modify("đã loại trường không được chính sách cho phép gửi hãng",
                                  payload=safe_payload)

    return Verdict.allow()
