# Phân công chặng cuối để hoàn thành & nộp LAB 10 (Thẻ S7)

> **Tình trạng hiện tại:**
> - `lab10.grade --incident S7` đã đạt **`PASS-VISIBLE`** (`1 integrity ✅`, `2 criteria ✅`, `3 visible ✅`, `5 regression ✅`, `6 monitor ✅` với metric `recipient_pii_fields_removed_rate`).
> - **Phiếu A** và **Phiếu B**: Đã `[ĐỦ]` mọi mục.
> - **Còn lại:** Hoàn tất **5 mục cuối của Phiếu C (`C6, C9, C10, C11, C12`)**, điền **`submission/submission.json`**, điền **`TEAM.md`**, chạy `check_submission --collect` tới **`ĐỦ THÀNH PHẦN`**, push bài và nộp LMS.

---

## 1. Phân công cụ thể cho 3 người (Chặng cuối)

| Vai | Thành viên | Việc còn lại phải làm ngay |
| :--- | :--- | :--- |
| **1. Kỹ sư cổng** | **Trịnh Thanh Tùng** | 1. Kiểm tra lại **C0** (dòng 2–4 với mã lần chạy mới nhất `R-S7-grade-20261118-222829-05580d` / `R-S7-after-20261118-222830-05580d`).<br>2. Cùng chốt **C6** (Fault tree trước sửa) nếu cần bổ sung bằng chứng code.<br>3. Tự viết mục cá nhân `## TrinhThanhTung-<MSSV>` trong `TEAM.md` + nộp link repo lên LMS. |
| **2. Sản phẩm & Kinh doanh** | **Đặng Nhật Long** | 1. Cùng chốt **C6** (Fault tree trước sửa).<br>2. **Chủ trì điền C12** (Quyết định Gate 1 **v2**, bảng 3 mốc `base · prepared · after`, phân khúc xấu nhất, và **3 dòng bắt buộc**).<br>3. Tự viết mục cá nhân `## DangNhatLong-<MSSV>` trong `TEAM.md` + nộp link repo lên LMS. |
| **3. Vận hành & Pháp lý (Máy chính)** | **Đinh Trần Nguyên** | 1. Kiểm tra & điền lại **C6** (nếu bị ghi đè/còn nguyên mẫu).<br>2. Điền **C9** (Fault tree sau sửa), **C10** (Risk register ≥ 1 dòng), **C11** (cập nhật Checklist 9 nhóm có PIC + viết Runbook phần 4–5).<br>3. Điền **`submission/submission.json`** (`team`, `members` dạng `"HoVaTen-MSSV"`, `incident: "S7"`, `decision_v1`, `decision_v2`, `three_lines` chép từ C12).<br>4. Điền bảng thành viên & mục cá nhân `## DinhTranNguyen-<MSSV>` trong `TEAM.md`.<br>5. Chạy `python -m lab10.grade --incident S7` và `python -m lab10.check_submission --collect` tới khi ra **`ĐỦ THÀNH PHẦN`**, rồi `git commit` & `git push`.<br>6. Nộp link repo lên LMS. |

---

## 2. Thứ tự chạy nhanh để chốt bài (15 phút)

1. **Bước 1 (Làm chung 5 phút):** Chốt **C6** và **C12** (Quyết định v2 + 3 dòng bắt buộc) trong `templates/form-c-incident.md`.
2. **Bước 2 (Nguyên — Máy chính):** Điền **C9, C10, C11** trong `templates/form-c-incident.md` và điền **`submission/submission.json`**.
3. **Bước 3 (Cả 3 người):** Gửi đủ **MSSV** để điền bảng thành viên trong `TEAM.md` và mỗi người viết mục cá nhân `## HoVaTen-MSSV` (kèm Exit ticket).
4. **Bước 4 (Nguyên — Máy chính):** Chạy kiểm tra cuối:
   ```powershell
   python -m lab10.grade --incident S7
   python -m lab10.check_submission --collect
   ```
   Đảm bảo dòng cuối in **`ĐỦ THÀNH PHẦN`**, rồi đẩy lên GitHub:
   ```powershell
   git add -u
   git add submission templates TEAM.md
   git commit -m "LAB 10: bai nop"
   git push -u origin main
   ```
5. **Bước 5 (Từng thành viên):** Mỗi người tự nộp link repo `https://github.com/nguyentrandinh-hub/K5-L3A-DAY10-ahihi-PoCtoPilotGate1` trên LMS trước deadline.
