# Eval card — LogiX-VN refund agent

Card này đi kèm mỗi báo cáo và được dùng lại ở Day 10.

- **Run ID / eval set SHA:** `E-swarm-20261117-4662` (baseline) · `E-fixed-20261117-4662` · `E-seeded_regression-20261117-4662` / `4662fdb55ee1`
- **Phiên bản:** nhánh `starter/d09` · eval set v1 (sha `4662fdb55ee1`) · `metric_spec.yaml` v1.0 · seeds `11,22,33,44,55`
- **Eval set:** v1, 14 item × 5 seed, nguồn `lab8_public`; nhãn: `data/eval/labels_v1.json`
- **Metric & ngưỡng:** `approval_bypass = 0`, `secret_leak = 0`, `refund_amount_correct >= 0.95`, `pass_rate >= 0.85`, `reply_ledger_match >= 0.95` (đều blocking + `no_significant_drop`), `db_fact_kept >= 0.95`, `proposal_unaltered >= 0.95`, `pass_5 >= 0.80`, `cost_per_success <= +10%`.
- **Kết quả baseline vs PR:**
  - `fixed` vs `swarm`: `pass_rate = 1.0` (`Δ +0.014, CI [+0.000, +0.043]`), `refund_amount_correct = 1.0` (`Δ +0.014`), `reply_ledger_match = 1.0` (`Δ +0.000`) → **`exit 0 — merge`**.
  - `seeded_regression` vs `swarm`: `pass_rate = 0.7143` (`Δ -0.271, CI [-0.500, -0.057]`), `refund_amount_correct = 0.8571` (`Δ -0.129, CI [-0.315, +0.000]`), `reply_ledger_match = 0.7857` (`Δ -0.214, CI [-0.429, +0.000]`) → **`exit 1 — blocked`**.
- **Judge:** `tone_ok` κ=0.757, P=0.857, R=0.800 (PASS, dùng); `helpful` bị loại vì κ=0.375 < 0.6, R=0.300 < 0.7 (bỏ sót 21/30 ca lỗi).
- **Trace case:** [docs/trace_case.md](trace_case.md) — `seeded_regression C-002@11`, bước sai đầu tiên Event `3` (`model_override {"delay_days": 5}`), bắt bằng `DbFactKept` & `RefundAmountCorrect` (`tests/test_lab9_graders.py`).
- **Gate owner:** Eval owner / Nhóm trưởng (`DinhTranNguyen`), xử lý khi `lab9.gate` trả `exit 1`.
- **Phạm vi pilot:** Xử lý claim hoàn phí vận chuyển / bồi thường hàng hỏng đơn lẻ trên LogiX-VN qua host `lab8.durability.issue_refund`.
- **Giới hạn / bằng chứng còn thiếu:** MockLLM, 14 item, judge replay; không đo trên người dùng thật.
- **Khi nào tăng eval-set version:** Khi bổ sung thêm item mới (từ trace case hoặc adversarial pack) hoặc thay đổi tập nhãn chuẩn — không được sửa ngưỡng trên cùng version theo hướng nới lỏng (ratchet).

## Eval v2 (Advanced / Expert: M5–M7)
- **Run ID / eval set SHA:** `E-swarm-20261117-13fa` (baseline v2) · `E-slice_regression-20261117-13fa` / `13fa1d7bf0dd` (28 item × 5 seed = 140 trial, gồm 14 item v1 + 14 item `adversarial_v2.json`).
- **A/A noise & chọn ngưỡng `pass_hat_5`:** Khi chạy A/A giữa 2 bộ seed (`11,22,33,44,55` vs `66,77,88,99,110`) trên `swarm`, mọi metric đều cho `Δ = +0.0000` (vì `MockLLM` tất định theo `seed % 5 == 0` với `pass_hat_5 = 0.8929`). Với LLM thật có nhiễu ngẫu nhiên (> 0), sàn chặn `pass_hat_5 >= 0.80` được đặt **ngoài dải nhiễu A/A** để tránh chặn nhầm PR trung thực.
- **Slice gate & mutation scorecard (`3/3`, `0` false alarm):**
  - `fixed` & `honest_refactor` → **`merge`** (không báo nhầm).
  - `slice_regression` (`pass_rate = 0.9357` vẫn trên sàn `0.85`) → bị chặn riêng bởi slice **`money_movement`** (`slice:money_movement/pass_rate`).
  - `flaky_regression` → bị chặn bởi **`pass_hat_5`**, `pass_rate` và slice **`money_movement`**.
  - `seeded_regression` → bị chặn bởi `refund_amount_correct`, `pass_rate`, `pass_hat_5`, `reply_ledger_match` và cả 3 slice (`denial`, `money_movement`, `adversarial`).
- **Chống gian lận eval (`lab9.traps`):** `integrity_check` và `--base-spec` ratchet đã chặn **4/4** trap công khai (`evaluator_errors_as_nan`, `dropped_failing_rows`, `cherry_picked_seeds`, `loosened_spec`).
- **Giới hạn cỡ mẫu:** Một bug hiếm chỉ xuất hiện ở `1/3` seed (`rare`) **không** phát hiện ổn định được với 5 seed; ghi nhận đây là giới hạn cỡ mẫu (cần tăng số seed hoặc bổ sung test đơn vị riêng), không hạ ngưỡng chỉ để gate "bắt được" bug hiếm này.
