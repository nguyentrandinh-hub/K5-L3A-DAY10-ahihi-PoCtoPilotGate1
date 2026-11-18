"""★ FILE ĐỘI SỬA (2/3): chỉ số theo dõi (monitor). Thêm ÍT NHẤT MỘT chỉ số bắt được sự cố của bàn.

Mỗi monitor nhận danh sách trial (KHÔNG có nhãn đúng/sai, giống production) và trả về một số.
Một trial = {"ticket_id", "seed", "day", "status", "amount_vnd", "ticket", "events", "ledger", "faults", "outbound",
             "arrive_min", "warehouse", "cost_vnd", "review_kind", "queue_wait_min", "queue_stuck"}
  "day"            một ngày vận hành giả lập: các ticket cùng "day" và cùng "seed" chạy nối nhau trên cùng một sổ cái
  "arrive_min"     phút ticket tới trong ca (0..480)          "warehouse"   kho của đơn
  "cost_vnd"       tiền LLM + nền tảng đã tốn cho ticket      "review_kind" None / "escalated" (trợ lý chuyển người) /
  "queue_wait_min" số phút chờ người duyệt (None nếu không vào hàng chờ)     "recheck" (nhân viên tự kiểm lại)
Chỉ số có thể là kỹ thuật (tỉ lệ model đè số trong ticket lên DB), vận hành (số ca cần người trong giờ đông nhất),
hay kinh doanh (tỉ lệ ticket trợ lý đọc xong vẫn phải chuyển người).

lab10.grade kiểm: monitor chạy không lỗi, và giá trị trên gói sự cố khác giá trị trên bộ nền,
tức là monitor "sáng đèn" khi sự cố xảy ra.
"""


def escalation_rate(trials):
    return sum(t["status"] == "escalated" for t in trials) / max(1, len(trials))


def recipient_pii_fields_removed_rate(trials):
    """Share of carrier notices where the guard removed a recipient-identifying field."""
    notices = 0
    recipient_fields = {"recipient_contact", "recipient_name", "recipient_phone",
                        "recipient_address", "name", "phone", "street", "city"}
    affected = 0
    for trial in trials:
        events = trial.get("events", [])
        has_notice = any(e.get("type") == "tool" and e.get("tool") == "notify_carrier" for e in events)
        if has_notice:
            notices += 1
            guard_events = [e for e in events
                            if e.get("type") == "guard" and e.get("kind") == "guard_carrier_notice_fields_removed"]
            removed = {field for e in guard_events for field in e.get("removed_fields", [])}
            value_pii_removed = any(e.get("recipient_pii_value_fields") for e in guard_events)
            if removed & recipient_fields or value_pii_removed:
                affected += 1
    return affected / max(1, notices)


MONITORS = {
    "escalation_rate": escalation_rate,     # có sẵn; KHÔNG tính là metric mới của đội
    "recipient_pii_fields_removed_rate": recipient_pii_fields_removed_rate,
}
STARTER_MONITORS = ("escalation_rate",)
