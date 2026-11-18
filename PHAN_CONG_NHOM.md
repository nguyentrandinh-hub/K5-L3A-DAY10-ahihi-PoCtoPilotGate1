# Phân công nhóm 3 người · LAB 10 (From PoC to Pilot · Gate 1)

> **Nhóm:** `ahihi` (`K5-L3A-DAY10-ahihi-PoCtoPilotGate1`) · **Thẻ sự cố đã bốc:** **`S7` (Lộ số điện thoại / thông tin người nhận quà)**
> **Quy tắc chung:** Làm song song phần riêng, hợp nhất tại các **điểm đồng bộ (⏳)**. Tuyệt đối không sửa các file bị khóa hash (`lab10/` trừ `guards.py` và `monitors.py`, `data/`, `tests/`, `incidents/`).

---

## 1. Bảng phân vai

| Vai | Thành viên | File chính phụ trách |
| :--- | :--- | :--- |
| **1. Kỹ sư cổng** | **Trịnh Thanh Tùng** | `lab10/guards.py`, `lab10/monitors.py`, chạy các lệnh CLI |
| **2. Sản phẩm & Kinh doanh** | **Đặng Nhật Long** | `config/acceptance_criteria.json`, `config/operating_gates.json` (`business`), Phiếu A, mục B8, mục C12 |
| **3. Vận hành & Pháp lý (Máy chính)** | **Đinh Trần Nguyên** | `config/operating_gates.json` (`operations`, `legal`), Phiếu B (`B4–B5`, `B7.5–B7.6`), Phiếu C (`C3–C4`, `C9–C11`), `submission/submission.json` |

---

## 2. Tiến độ CP1–CP3 (Đã hoàn thành ✅)

- [x] **CP1 · Phút 0–15:** Cài đặt repo, gắn `upstream`, cấu hình git, chạy `unittest` (`13 tests OK`), chia 3 vai.
- [x] **CP2 · Phút 15–65:** Hoàn thành Phiếu A ([templates/form-a-criteria.md](templates/form-a-criteria.md)), điền & ký `config/acceptance_criteria.json` (commit `f5c95da`, hash `4adc9a11`).
- [x] **CP3 · Phút 65–115:** Hoàn thành Phiếu B ([templates/form-b-evaluation-gates.md](templates/form-b-evaluation-gates.md)), code 3 cổng vòng 1 trong `lab10/guards.py`, điền `config/operating_gates.json`, chốt mốc `prepared` (`108eba30`) và quyết định **v1: Thu hẹp** (2 kho `HN`, `HCM`).

---

## 3. Kế hoạch chi tiết CP4 · Khối 3: Sự cố **S7** (Phút 125–185)

### Bước 0 · Nhận thẻ & đo mốc `prepared` (Phút 125–135) — **Đã chạy lần đầu**
- [x] Đã giải nén thẻ, ghi `Thẻ đã bốc: S7` vào đầu Phiếu C và chạy `python -m lab10.grade --incident S7` (`R-S7-grade-20261118-164605-aa738b`).
- [ ] **Máy chính (Đinh Trần Nguyên):** Fix lỗi `1 integrity ❌` (do Windows `core.autocrlf = true` đổi LF → CRLF ở các file khóa trong `MANIFEST.json`).
- [ ] **Cả 3 người:** Điền **C0** (mã lần chạy `base`, `prepared`) và **C1** (cổng vòng 1 `notify_carrier` whitelist đã chặn sạch `30` ca lộ PII ở `prepared`, đưa `pass_rate` từ `0.25` lên `1.0`; đối chiếu lại mục B6).

---

### Bước 1–4 · Phân tích sự cố S7 (Phút 135–155)

- **Làm song song (Phút 135–149):**
  - [ ] **Kỹ sư cổng (Trịnh Thanh Tùng):**
    - Dò trace mốc `base` trên ≥ 2 ticket hỏng khác kiểu trong bộ S7: `S7-01`, `S7-04`, `S7-20`, `S7-21` và đối chứng `S7-05` (`python -m lab10.trace --suite S7 --ticket <ID> --seed 11`).
    - Tìm bước sai đầu tiên (dòng `GỬI HÃNG` / `notify_carrier` payload lấy từ đâu, kể cả khi khách không gõ SĐT vào ticket).
    - Điền bảng soát lỗi và mô tả tác hại vào **Mục C2** (câu 3.1).
  - [ ] **Vận hành & Pháp lý (Đinh Trần Nguyên):**
    - Làm **Mục C3 (phần riêng S7: `C3.3 Hiệu chỉnh lòng tin`)**: điền 2 mốc *tin quá mức* và *không tin* cho **người đặt hàng** và **người nhận quà**, nêu rõ dữ liệu nào rời hệ thống mà họ không biết.
    - Làm **Mục C4 (`HAZOP của thẻ S7`)**: ít nhất **3 dòng** (không ghi đè HAZOP vòng 1 ở Phiếu B), tập trung vào `notify_carrier` / `recipient` / `is_gift` / rò rỉ gián tiếp.
    - Điền câu **3.3 (Giả định môi trường)** ở **Mục C5** (ví dụ: giả định người nhận quà đã đồng ý chia sẻ SĐT/địa chỉ cho hãng, hoặc giả định danh sách `pii_fields_blocked_to_third_party` đủ phủ mọi tên trường).
  - [ ] **Sản phẩm & Kinh doanh (Đặng Nhật Long):**
    - Điền câu **3.2 (Specification)** ở **Mục C5**: phát biểu spec cho kênh gửi hãng (chỉ các trường nằm trong `policies[].carrier_notice_fields`: `order_id`, `parcel_id`, `district`, `delay_days` mới được phép rời hệ thống, kiểm được bằng code/report).
- **Làm chung (Phút 149–155):**
  - [ ] **Cả 3 người:** Vẽ **Fault tree trước khi sửa** ở **Mục C6** (sự kiện đỉnh: *Lộ SĐT/địa chỉ người nhận quà cho hãng vận chuyển*; ít nhất 2 nhánh ở 2 tầng khác nhau: Kỹ thuật + Pháp lý/Quy trình; mỗi lá có bằng chứng `S7-xx@11`, trường dữ liệu `orders[].recipient`, hoặc dòng report).

---

### Bước 5–8 · Sửa, thêm Monitor & Cập nhật tài liệu (Phút 155–185)

- **Làm song song (Phút 155–180):**
  - [ ] **Kỹ sư cổng (Trịnh Thanh Tùng):**
    - Kiểm tra & gia cố `lab10/guards.py` (đảm bảo chặn/lọc chắc chắn cho cả test ẩn: không để lọt trường ngoài `carrier_notice_fields` ở `notify_carrier`, kiểm tra giá trị PII nếu lọt vào chuỗi).
    - **Bắt buộc (`6 monitor ❌`):** Thêm ít nhất **1 hàm chỉ số theo dõi mới** vào `lab10/monitors.py` và đăng ký vào dict `MONITORS` (bắt được sự cố S7 — ví dụ đo tỉ lệ/số lần `guard_carrier_notice_fields_removed` hoặc `legal_gate` chặn trường lạ/PII). Điền **Mục C7** (cột code) và **Mục C8** (3 ô Thước đo → Dữ liệu → Cách tính).
  - [ ] **Sản phẩm & Kinh doanh (Đặng Nhật Long):**
    - Rà lại `config/operating_gates.json` mục `business` trên bảng 3 mốc S7 (độ phủ hiện tại `0.75` trên S7, ROI `0.76`, chi phí `5.667đ` < `8.500đ`, không vượt trần). Điền **Mục C7** (nếu giữ hoặc chỉnh phạm vi).
  - [ ] **Vận hành & Pháp lý (Đinh Trần Nguyên):**
    - Rà `config/operating_gates.json` mục `legal`: bổ sung thêm tên trường PII liên quan đến người nhận nếu cần (`"recipient"`, `"recipient_name"`, `"recipient_phone"`, `"recipient_address"`, `"city"`) vào `pii_fields_blocked_to_third_party` để bảo vệ nhiều lớp cùng `guards.py`. Điền **Mục C7** (cột vận hành/pháp lý).

- ⏳ **ĐIỂM ĐỢI #4 (Phút 180–185) — Kiểm tra lại toàn bộ & hoàn tất C9–C11:**
  - [ ] **Máy chính / Kỹ sư cổng** chạy:
    ```powershell
    python -m lab10.eval --suite S7 --stage after --note "S7: them monitor va gia co loc PII"
    python -m lab10.eval --suite base --stage after --note "kiem regression sau sua S7"
    python -m lab10.grade --incident S7
    ```
  - [ ] Kiểm tra report đạt đủ: `1 integrity ✅`, `2 criteria ✅`, `3 visible ✅`, `5 regression ✅`, `6 monitor ✅`.
  - [ ] **Vận hành & Pháp lý (Đinh Trần Nguyên):** Dựa vào kết quả mới nhất để điền:
    - **Mục C9:** Cập nhật Fault tree sau khi sửa (nêu rõ cổng nằm ở nhánh nào, tầng nào — *bảo đảm/ngăn hẳn* bằng whitelist, nhánh nào còn hở).
    - **Mục C10:** Thêm ≥ 1 dòng **Risk register** (ví dụ: rò rỉ dữ liệu qua giá trị nằm trong trường hợp lệ hoặc kênh khác ngoài `notify_carrier`).
    - **Mục C11:** Cập nhật **Checklist 9 nhóm việc** (trạng thái mới + PIC có tên cụ thể) và viết **Runbook phần 4–5**.

---

## 4. Kế hoạch CP5 · Quyết định v2, Demo & Nộp bài (Phút 185–240)

- [ ] **Cả 3 người (Đặng Nhật Long cầm bút chính):** Điền **Mục C12** (Quyết định **v2** — so sánh với v1, ghi mã lần chạy 3 mốc, phân khúc xấu nhất, và **3 dòng bắt buộc** bám sát gợi ý mặt sau thẻ S7).
- [ ] **Vận hành & Pháp lý (Đinh Trần Nguyên):**
  - Điền `submission/submission.json` (`team: "K5-L3A-DAY10-ahihi-PoCtoPilotGate1"`, `members` dạng `"HoVaTen-MSSV"`, `incident: "S7"`, `decision_v1`, `decision_v2`, `three_lines` chép từ C12).
  - Chạy `python -m lab10.check_submission --collect` và sửa mọi mục `[THIẾU]` tới khi in **`ĐỦ THÀNH PHẦN`**.
- [ ] **Cả 3 người (Phút 200–230):** Demo 3 mốc & phản biện. *(Nếu demo có đổi thử số trong `operating_gates.json`, nhớ trả lại bản v2 rồi chạy lại `grade --incident S7` và `check_submission --collect`).*
- [ ] **Cả 3 thành viên (trước phút 240 / deadline):**
  - Điền bảng thành viên và **mỗi người tự viết mục cá nhân `## HoVaTen-MSSV`** (kèm Exit ticket) trong `TEAM.md`.
  - Commit & Push cuối buổi:
    ```powershell
    git add -u
    git add submission templates TEAM.md
    git commit -m "LAB 10: bai nop"
    git push -u origin main
    ```
  - **Mỗi thành viên tự nộp link repo trên LMS bằng tài khoản cá nhân.**
