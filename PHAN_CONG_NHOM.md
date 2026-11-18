# Phân công nhóm 3 người · LAB 10 (From PoC to Pilot · Gate 1)

> **Quy tắc chung:** Làm song song phần riêng, hợp nhất tại **4 điểm đồng bộ (⏳)**. Tuyệt đối không sửa các file bị khóa hash (`lab10/` trừ `guards.py` và `monitors.py`, `data/`, `tests/`, `incidents/`).

---

## 1. Bảng phân vai

| Vai | Thành viên (Họ tên - MSSV) | File chính phụ trách |
| :--- | :--- | :--- |
| **1. Kỹ sư cổng** | *(Điền tên - MSSV)* | `lab10/guards.py`, `lab10/monitors.py`, chạy các lệnh CLI |
| **2. Sản phẩm & Kinh doanh** | *(Điền tên - MSSV)* | `config/acceptance_criteria.json`, `config/operating_gates.json` (`business`), Phiếu A, mục B8, mục C12 |
| **3. Vận hành & Pháp lý** | *(Điền tên - MSSV)* | `config/operating_gates.json` (`operations`, `legal`), Phiếu B (`B4–B5`, `B7.5–B7.6`), Phiếu C (`C3–C4`, `C9–C11`), `submission/submission.json` |

---

## 2. Lịch làm việc theo 5 Checkpoint (0–240 phút)

### CP1 · Phút 0–15: Cài đặt & chia vai
- [ ] **Trưởng nhóm (hoặc Kỹ sư cổng):**
  - Đảm bảo repo Private, đã mời tài khoản team chấm quyền **Read**.
  - Gắn `upstream`: `git remote add upstream https://github.com/VinUni-AI20k/K5_L3_Day10_PoC-to-Pilot_Gate1_student.git`
  - Đặt danh tính Git bằng MSSV: `git config user.name "<MSSV>"` và `git config user.email "<MSSV>@example.com"`
  - Chạy `python -m unittest discover -s tests` → `Ran 13 tests ... OK`.
- [ ] **SP&KD + VH&PL:** Mở sẵn Eval card và PRD v1.1 từ Lab 9; điền bảng thành viên vào `TEAM.md`.

---

### CP2 · Phút 15–65: Khối 1 — Viết tiêu chí & Ký (Phiếu A)
> ⚠️ **KHÔNG chạy `lab10.eval` trước khi ký xong!**

- **Làm song song (Phút 15–55):**
  - [ ] **SP&KD:** Câu `1.1` (A1) · Câu `1.6` (A4 + ranh giới đầu ra) · Điền `config/acceptance_criteria.json` (xem gợi ý trong `data/world.json` → `ops_facts`, không chép ngưỡng từ file example).
  - [ ] **VH&PL:** Câu `1.2` (A1: góc nhìn chị Oanh, chị Hạnh) · Câu `1.4` (A2: cột Telemetry production).
  - [ ] **Kỹ sư cổng:** Câu `1.3` (A2: cột Offline metric cho 1 bước của agent).
- **Làm chung (Phút 55–60):**
  - [ ] **Cả 3 người:** Chốt câu `1.5` (A3) và rà lại toàn bộ `config/acceptance_criteria.json`.
- ⏳ **ĐIỂM ĐỢI #1 (Phút 60–65) — Ký tiêu chí:**
  - [ ] Đợi **SP&KD** chốt xong `acceptance_criteria.json`.
  - [ ] **Kỹ sư cổng** chạy:
    ```bash
    python -m lab10.criteria sign
    git add config/acceptance_criteria.json config/acceptance_criteria.lock && git commit -m "Sign acceptance criteria" && git push -u origin main
    ```
  - [ ] Ghi giờ ký và mã commit vào **Phiếu A mục A5**. *(Từ đây không sửa `acceptance_criteria.json` nữa).*

---

### CP3 · Phút 65–115: Khối 2 — Đo, tìm rủi ro, cổng vòng 1 & quyết định v1 (Phiếu B)

#### Khối 2A (Phút 65–85): Đo & Tìm rủi ro
- **Làm song song (Phút 65–75):**
  - [ ] **Kỹ sư cổng:** Chạy mốc `base`, `gate` (`2.1`, mục B1 & dòng 1 của B0) và dò `T-002@55` (`2.2`, mục B2):
    ```bash
    python -m lab10.eval --suite base --stage base --note "baseline"
    python -m lab10.gate --run runs/<mã_lần_chạy>/report.json
    python -m lab10.trace --suite base --ticket T-002 --seed 55
    ```
  - [ ] **SP&KD:** Câu `2.3` (B3: bản đồ dữ liệu + 1 ví dụ drift từ `data/world.json`).
  - [ ] **VH&PL:** Câu `2.4` (B4: HAZOP vòng 1 ≥ 3 dòng + ≥ 2 dòng ngoài kỹ thuật; B5: checklist 9 nhóm có PIC cụ thể).
- **Làm chung (Phút 75–85):**
  - [ ] **Cả 3 người:** Câu `2.5` (B6: Pre-mortem 4 lăng kính), chọn **2–3 lý do** để làm cổng phòng ngừa.

#### Khối 2B (Phút 85–105): Dựng cổng phòng ngừa
- **Làm song song:**
  - [ ] **Kỹ sư cổng:** Câu `2.6` (code 2–3 cổng trong `lab10/guards.py`), Câu `2.7` (B7.2: 2 bước tránh rò rỉ dữ liệu), Câu `2.8` (cùng **SP&KD** hoặc **VH&PL** viết 2 ticket hiểm chạy `--adhoc` ở B7.3).
  - [ ] **SP&KD:** Câu `2.9` (B7.4 + điền `config/operating_gates.json` mục `business`).
  - [ ] **VH&PL:** Câu `2.10` (điền `config/operating_gates.json` mục `operations`, `legal` + viết Runbook phần 1–3 ở B7.5 và Giờ cao điểm ở B7.6).

#### Chốt Vòng 1 (Phút 105–115)
- ⏳ **ĐIỂM ĐỢI #2 — Chốt `prepared` & quyết định v1:**
  - [ ] Đợi cả 3 xong `guards.py` và `operating_gates.json` (`operations.pic` không trống, test xanh).
  - [ ] **Kỹ sư cổng** chạy:
    ```bash
    python -m lab10.eval --suite base --stage after --note "cổng vòng 1"
    python -m unittest discover -s tests
    python -m lab10.checkpoint
    python -m lab10.eval --suite base --stage prepared
    python -m lab10.gate --run runs/<mã_lần_chạy>/report.json
    ```
  - [ ] **Cả 3 người (SP&KD cầm bút):** Điền cột **v1** ở **Phiếu B mục B8**, rồi commit & push.

---

### CP4 · Phút 125–185: Khối 3 — Sự cố & Sửa (Phiếu C)

#### Nhận thẻ & đo `prepared` (Phút 125–135)
- ⏳ **ĐIỂM ĐỢI #3 — Kéo thẻ & chạy mốc `prepared`:**
  - [ ] **Kỹ sư cổng** kéo thẻ: `git pull --no-rebase --no-edit --allow-unrelated-histories -X ours upstream main`
  - [ ] Bốc số thẻ (`S1`–`S8`), ghi vào dòng `Thẻ đã bốc:` ở đầu **Phiếu C** và `TEAM.md`.
  - [ ] Chạy ngay trước khi sửa gì: `python -m lab10.grade --incident Sx`
  - [ ] **Cả 3 người:** Đọc kết quả, điền mục C0 và C1 (`3.0`).

#### Phân tích sự cố (Phút 135–155)
- **Làm song song (Phút 135–149):**
  - [ ] **Kỹ sư cổng:** Dò `trace` ≥ 2 ticket hỏng khác kiểu (`python -m lab10.trace --suite Sx --ticket <ID> --seed 11`) → điền bảng soát lỗi C2 (`3.1`).
  - [ ] **VH&PL:** Làm phần riêng theo thẻ ở C3 (trừ thẻ S4), HAZOP của thẻ ở C4 (`3.1`), giả định môi trường ở C5 (`3.3`).
  - [ ] **SP&KD:** Viết specification ở C5 (`3.2`).
- **Làm chung (Phút 149–155):**
  - [ ] **Cả 3 người:** Vẽ **Fault tree trước khi sửa** ở mục C6 (`3.4`, có bằng chứng ở mỗi lá).

#### Sửa & Thêm chỉ số theo dõi (Phút 155–185)
- **Làm song song (Phút 155–180):**
  - [ ] **Kỹ sư cổng:** Sửa `lab10/guards.py` + thêm ít nhất 1 metric mới vào `lab10/monitors.py` (`3.5`, `3.6`, điền C7–C8).
  - [ ] **SP&KD:** Chỉnh `config/operating_gates.json` mục `business` (`3.5`, điền C7).
  - [ ] **VH&PL:** Chỉnh `config/operating_gates.json` mục `operations`, `legal` (`3.5`, điền C7).
- ⏳ **ĐIỂM ĐỢI #4 (Phút 180–185) — Kiểm tra lại & cập nhật tài liệu:**
  - [ ] **Kỹ sư cổng** chạy:
    ```bash
    python -m lab10.eval --suite Sx --stage after --note "sửa sự cố"
    python -m lab10.eval --suite base --stage after --note "kiểm regression"
    python -m lab10.grade --incident Sx
    ```
  - [ ] Đợi report báo `integrity ✅`, `criteria ✅`, `visible ✅`, `regression ✅`, `monitor ✅`.
  - [ ] **VH&PL:** Dựa vào kết quả mới nhất để điền C9 (Fault tree sau sửa), C10 (Risk register), C11 (cập nhật checklist + Runbook phần 4–5).

---

### CP5 · Phút 185–240: Quyết định v2, Demo & Nộp bài
- [ ] **Cả 3 người (SP&KD cầm bút):** Chốt quyết định **v2** và **3 dòng bắt buộc** ở Phiếu C mục C12 (khớp với bảng 3 mốc của `grade`).
- [ ] **VH&PL:** Điền `submission/submission.json` (`members` dạng `"HoVaTen-MSSV"`), chạy `python -m lab10.check_submission --collect` tới khi ra `ĐỦ THÀNH PHẦN`.
- [ ] **Cả 3 người (Phút 200–230):** Demo 3 mốc & phản biện. *(Nếu demo có sửa thử số trong config thì nhớ trả về bản v2, chạy lại `grade` và `check_submission --collect`).*
- [ ] **Từng thành viên (trước phút 240 / deadline):**
  - Tự viết mục cá nhân `## HoVaTen-MSSV` (kèm Exit ticket) trong `TEAM.md`.
  - Push bài lần cuối: `git add -u && git add submission templates TEAM.md && git commit -m "LAB 10: bài nộp" && git push -u origin main`
  - **Mỗi người tự nộp link repo lên LMS bằng tài khoản cá nhân.**

---

## 3. Quy tắc tránh xung đột Git (Conflict)
- **Nếu làm chung trên 1 máy (Khuyên dùng):** Dùng máy của **Kỹ sư cổng** làm máy chính để chạy lệnh và nhập code/config; **SP&KD** và **VH&PL** soạn nội dung phiếu ra nháp rồi gộp vào `templates/form-*.md` và `config/operating_gates.json`.
- **Nếu làm trên 3 máy riêng:** Luôn `git pull` trước khi sửa/push và giữ nguyên tắc không sửa trùng file cùng lúc:
  - Khối 1: SP&KD giữ `acceptance_criteria.json`.
  - Khối 2 & 3: Kỹ sư cổng giữ `lab10/guards.py` + `monitors.py`; SP&KD gửi số `business` cho VH&PL nhập chung vào `operating_gates.json`.
