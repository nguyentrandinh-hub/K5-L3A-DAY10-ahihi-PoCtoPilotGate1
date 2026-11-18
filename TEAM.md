# Team

## Thông tin nhóm

- Tên nhóm (`TenNhom`, không dấu, không khoảng trắng): ahihi
- Lớp: `L3A`
- Repo của bàn: `K5-L3A-DAY10-ahihi-PoCtoPilotGate1`
- Thẻ sự cố đã bốc (S1–S8): `S7`

## Thành viên

Họ tên đầy đủ và MSSV của **mọi** thành viên; thêm dòng nếu cần. Vai: Kỹ sư cổng · Sản phẩm và kinh doanh · Vận hành và pháp lý (README mục 3, phút 0–15).

| STT | Họ và tên | MSSV | Vai | Trưởng nhóm |
| --: | --------- | ---- | --- | :---------: |
|   1 | Đinh Trần Nguyên | 2A202603517 | Vận hành và pháp lý | x |
|   2 | Trịnh Thanh Tùng | 2A202603456 | Kỹ sư cổng | |
|   3 | Đặng Long Nhật | 2A202603483 | Sản phẩm và kinh doanh | |

Ghi `members` trong `submission/submission.json` theo dạng `"HoVaTen-MSSV"`, khớp bảng trên.

## Cá nhân

Mỗi thành viên tự viết một mục bên dưới (chép mẫu, đổi tiêu đề thành họ tên không dấu và MSSV, ví dụ `## NguyenVanAn-20241234`).

## DinhTranNguyen-2A202603517

### Phần việc phụ trách

- Vai: **Vận hành và pháp lý** (kiêm máy chính điều phối gom bài nộp).
- Câu 1.2, 1.4 (Phiếu A); Câu 2.4 HAZOP vòng 1 & Checklist 9 nhóm (B4–B5), Câu 2.5 Pre-mortem (B6), Câu 2.10 cổng `operations` & `legal` trong `config/operating_gates.json` + Runbook 1–3 & Giờ cao điểm (B7.5–B7.6) ở Phiếu B; Câu 3.0–3.1 (`C0`, `C1`, `C3.3 Hiệu chỉnh lòng tin`, `C4 HAZOP thẻ S7`), Câu 3.3 Giả định môi trường (`C5`), Câu 3.4 Fault tree trước sửa (`C6`), Câu 3.7 (`C9`, `C10`, `C11`) ở Phiếu C; điền `submission/submission.json` và chạy `check_submission --collect`.

### Đóng góp cụ thể

- Thiết kế cấu hình `operations` (`NV-TUNG`, `NV-HANH`, `6 ca/giờ`, SLA `60 phút`, kênh `#logix-refund-ops-alerts`) và `legal` (`pii_fields_blocked_to_third_party`, `carrier_fault_requires_recorded_cause: true`) trong `config/operating_gates.json`.
- Viết toàn bộ Runbook 1–5, Giờ cao điểm, HAZOP vòng 1 & vòng 2 (S7), phân tích `C3.3 Hiệu chỉnh lòng tin` và cập nhật Checklist/Risk register.
- Kiểm tra và đồng bộ lại các file khóa hash (CRLF → LF) để đạt `1 integrity ✅`, hoàn thiện `submission/submission.json` và gom bài nộp.

### Bằng chứng

- Commit ký tiêu chí `f5c95da`; hash chốt vòng 1 `108eba30`; report `R-S7-grade-20261118-222829-05580d` (`PASS-VISIBLE`); `templates/form-b-evaluation-gates.md` (B4–B6, B7.5–B7.6); `templates/form-c-incident.md` (C1, C3.3, C4, C5, C6, C9–C11).

### Exit ticket

- **Điều học được:** Cổng bằng cấu hình (`legal.pii_fields_blocked_to_third_party`) kết hợp whitelist ở tầng `write_gate` giúp bảo đảm không lộ dữ liệu cho bên thứ ba (người nhận quà — người không dùng hệ thống) thay vì chỉ dò/che mẫu ký tự.
- **Điều còn chưa chắc:** Trên dữ liệu thật ngoài production, liệu trường `district` hoặc các kênh giao nhận ngoài `notify_carrier` có bị nhập lẫn SĐT/địa chỉ chi tiết mà chưa có kiểm soát đầu vào hay không.

## TrinhThanhTung-2A202603456

### Phần việc phụ trách

Kỹ sư cổng: B7.1 và gia cố `lab10/guards.py`; thêm monitor trong `lab10/monitors.py`; phân tích trace và điền C2, phần kỹ thuật C7–C9, C8 trong `templates/form-c-incident.md`.

### Đóng góp cụ thể

- Giữ `notify_carrier` theo allowlist của chính sách hiệu lực; lọc trường không được phép và kiểm tra giá trị payload có chứa tên, số điện thoại hoặc địa chỉ đã biết của người nhận.
- Thêm monitor `recipient_pii_fields_removed_rate` để theo dõi tỷ lệ thông báo hãng mà guard phải loại trường hoặc giá trị nhận diện người nhận.
- Dùng trace S7 để ghi nhận hai đường rò rỉ: PII từ nội dung ticket và `orders[].recipient` của đơn quà tặng; bổ sung nhánh kỹ thuật trong C9, gồm giới hạn còn lại là PII biến thể hoặc rời qua công cụ khác.

### Bằng chứng

- Commit code và tài liệu S7: `fe5bb296405fd7387cf2e0869f195ad13fbecfe6`.
- Chạy S7 after: `R-S7-after-20261118-172043-faf81d`; regression base: `R-base-after-20261118-172043-faf81d` (cả hai pass rate 1.0, theo report hiện có trong repo).
- Phiếu C: C2, C7, C8; góp ý nhánh kỹ thuật C9.

### Exit ticket

Điều học được: allowlist theo tên trường chưa đủ nếu giá trị của một trường được phép vẫn có thể chứa dữ liệu nhận diện; cần kiểm soát cả cấu trúc lẫn giá trị ở cổng gửi. Điều còn chưa chắc: cách so khớp giá trị hiện tại không nhận diện mọi cách viết lại hoặc suy diễn PII, và không bao phủ các kênh gửi ngoài `notify_carrier`; cần đánh giá thêm bằng test biến thể và dữ liệu pilot.

## DangLongNhat-2A202603483

### Phần việc phụ trách

Sản phẩm và kinh doanh của nhóm ahihi, thẻ S7. Phụ trách B3 (bản đồ dữ liệu và drift), B7.4 (cổng kinh doanh), C5 câu 3.2 (đặc tả kênh gửi hãng), rà phạm vi pilot ở C7 và chủ trì quyết định Gate 1 v2 ở C12. Phối hợp đối chiếu nguồn dữ liệu cá nhân trong cây lỗi C6.

### Đóng góp cụ thể

- Lập bản đồ nguồn dữ liệu của trợ lý hoàn tiền. Dùng trường hợp `REFUND-v4` có hiệu lực ngày 01/12/2026 để chỉ ra vì sao cần kiểm phiên bản chính sách trước khi ghi lỗi hãng đối với ca bất khả kháng.
- Giải trình các cổng kinh doanh gồm trần hoàn tự động **1.600.000đ/ngày**, ngân sách **1.350đ tiền máy/ticket**, phạm vi kho `HN` và `HCM`, cùng sàn ROI **0,15**.
- Viết đặc tả S7 cho `notify_carrier`. Payload gửi hãng chỉ gồm `order_id`, `parcel_id`, `district` và `delay_days`, với giá trị đối chiếu được với đơn hàng và tracking.
- Điền C12 gồm bảng `base · prepared · after`, phân khúc xấu nhất và ba dòng bắt buộc. Đề xuất giữ quyết định **Thu hẹp** như v1 vì phạm vi `HN` và `HCM` đạt độ phủ **75%** trên S7, chi phí **5.667đ/ticket** dưới trần **8.500đ** và ROI **0,76** trên sàn **0,15**.

### Bằng chứng

- Bản đồ dữ liệu, ví dụ drift và bốn cổng kinh doanh. [Phiếu B, B3 và B7.4](templates/form-b-evaluation-gates.md) · [Cấu hình business](config/operating_gates.json)
- Đặc tả kênh gửi hãng và quyết định Gate 1 v2. [Phiếu C, C5 và C12](templates/form-c-incident.md) · [Commit `ece5aa1` cập nhật C12](https://github.com/nguyentrandinh-hub/K5-L3A-DAY10-ahihi-PoCtoPilotGate1/commit/ece5aa1a442c5f100b62028bc5801d11cd9a26ec)
- Báo cáo `R-S7-grade-20261118-233355-2c66d9` đạt `PASS-VISIBLE`. Số lần lộ dữ liệu cá nhân qua ba mốc là **30 → 0 → 0**. Mốc sau sửa là `R-S7-after-20261118-233356-2c66d9`.
