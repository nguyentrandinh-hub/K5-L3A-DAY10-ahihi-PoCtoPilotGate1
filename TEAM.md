# Team

## Thông tin nhóm

- Tên nhóm (`TenNhom`, không dấu, không khoảng trắng):ahihi
- Lớp: `L3A`
- Repo của bàn: `K5-L3A-DAY10-ahihi-PoCtoPilotGate1`
- Thẻ sự cố đã bốc (S1–S8): `S7`

## Thành viên

Họ tên đầy đủ và MSSV của **mọi** thành viên; thêm dòng nếu cần. Vai: Kỹ sư cổng · Sản phẩm và kinh doanh · Vận hành và pháp lý (README mục 3, phút 0–15).

| STT | Họ và tên | MSSV | Vai | Trưởng nhóm |
| --: | --------- | ---- | --- | :---------: |
|   1 | Trịnh Thanh Tùng | 2A202603456 | Kỹ sư cổng |             |
|   2 |           |      |     |             |
|   3 |           |      |     |             |
|   4 |           |      |     |             |
|   5 |           |      |     |             |

Ghi `members` trong `submission/submission.json` theo dạng `"HoVaTen-MSSV"`, khớp bảng trên.

## Cá nhân

Mỗi thành viên tự viết một mục bên dưới (chép mẫu, đổi tiêu đề thành họ tên không dấu và MSSV, ví dụ `## NguyenVanAn-20241234`).

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
