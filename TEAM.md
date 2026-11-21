# Team

## Thông tin nhóm

- Tên nhóm: DLB
- Lớp: L3A
- Repo nhóm: K5-L3A-DAY13-DLB-LaunchEconomics
- URL repo, nhánh nộp, commit chốt: [https://github.com/NguyenQuangDao/K5-L3A-DAY13-DLB-LaunchEconomics](https://github.com/NguyenQuangDao/K5-L3A-DAY13-DLB-LaunchEconomics)

## Thành viên

| STT | Họ tên | MSSV | Email | GitHub | Vai trò |
| --: | ------ | ---- | ----- | ------ | ------- |
|   1 | Nguyễn Vũ Thành Long | 2A202603635 | 26ai.longnvt2@vinuni.edu.vn | - | Người viết code (CP1), Người kiểm số (CP2), pilot_plan.yaml (CP4) |
|   2 | Nguyễn Quang Đạo | 2A202603614 | 26ai.daonq2@vinuni.edu.vn | - | Người viết code (CP2), Người gắn nhãn 1 (CP3), kiểm số (CP1) |
|   3 | Nguyễn Gia Bảo | 2A202603647 | 26ai.baong5@vinuni.edu.vn | - | Người gắn nhãn 2 (CP3), giữ hồ sơ (CP5), kiểm số (CP4, CP5) |

Bốn vai của lab:

- **Người viết code:** viết và chạy `src/lab13.py`.
- **Người kiểm số:** tính tay một con số để đối chiếu, điền bảng.
- **Người gắn nhãn 1:** đọc đề, theo dõi điều kiện "Xong khi"; gắn nhãn 20 ca độc lập ở CP3.
- **Người gắn nhãn 2, kiêm giữ hồ sơ:** điền `report/team/ho_so_launch_v0.md` từ đầu buổi; gắn nhãn 20 ca độc lập ở CP3.

Đổi người viết code sau giờ giải lao, để ít nhất hai người trong nhóm tự tay tính được chi phí.

## Cá nhân

Mỗi thành viên đồng thời tạo một báo cáo riêng trong `report/` theo dạng:

```text
report/team/MSSV_HoTen.md
```

Ví dụ: `report/team/20241234_NguyenVanAn.md`.

Sao chép mục dưới đây cho từng thành viên.

## NguyễnVũThànhLong-2A202603635

### Phần việc phụ trách

- CP1: Người viết code (A1, `mo_hinh`, A3, A4)
- CP2: Viết code B1-B4 trong `src/lab13.py` và bảng B1-B4; kiểm số
- CP4: Code D1 và `pilot_plan.yaml`

### Đóng góp cụ thể

- Viết ba hàm A1 (ba phép thử ĐẠT), `mo_hinh`, bảng A2, A3, A4: chi phí mỗi việc thành công 4.472 đ [simulated], gấp 16,3 lần hoá đơn token
- Viết code độ nhạy B1-B4: xếp hạng làm lại > xem lại > lương; giới hạn 2 lần rẻ nhất cho công ty; xem lại 100% là 11.743 đ = 0,98× [simulated]
- Viết code D1 (1.251 · 3.103 · 1.000 · 300 · 299, power 0,64) và `kiem_tra_pilot_plan()`; viết lại `pilot_plan.yaml` với năm luật dừng đủ bốn vế
- Khôi phục bảng A1 và A4 bị ghi đè, xử lý xung đột `lab13.py`

### Bằng chứng

- Commit `71e2be4`, `31bd49c` (CP1), `f531cc7` (CP2), `49ff94f` (CP4)
- `src/lab13.py`, `report/team/bang_chi_phi.md`, `report/team/pilot_plan.yaml`
- Báo cáo cá nhân: `report/team/2A202603635_NguyenVuThanhLong.md`

## NguyễnQuangĐạo-2A202603614

### Phần việc phụ trách

- CP1: Kiểm số cho A, B
- CP2: Viết bảng độ nhạy B1-B4
- CP3: Người gắn nhãn 1 (20 ca độc lập)
- Kiểm số cho bảng A2, A3

### Đóng góp cụ thể

- Kiểm tay các con số trong bảng A2, A3
- Viết bảng độ nhạy B1-B4 trong bang_chi_phi.md
- Gắn nhãn 20 ca độc lập ở CP3
- So nhãn và tính tỉ lệ đồng thuận
- Ghi quy tắc phân biệt

### Bằng chứng

- report/team/bang_chi_phi.md có đầy đủ bảng B1-B4
- report/team/bang_loi.md có hai bộ nhãn, tỉ lệ đồng thuận 100%
- Bảng khắc phục 5 ca (mỗi loại 1 ca)
