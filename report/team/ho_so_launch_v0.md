# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

**Nhóm:** DLB  
**Người phụ trách:** Nguyễn Gia Bảo - 2A202603647
**Ngày tạo:** 21/11/2026  
**Đề xuất:** Go có điều kiện

Nhóm: DLB · Lớp: L3A

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | 4.472 đ/việc thành công [simulated] (= 4.373.585 đ [simulated] ÷ 978 việc), gấp 16,3× [simulated] hoá đơn token + tool chia số yêu cầu (274,7 đ, đo từ trace). Làm lại chiếm 51,8% [simulated], xem lại 40,7% [simulated] tổng chi phí | Giả lập | Kỹ sư trưởng agent |
| 2 · Ba yếu tố nhạy nhất | 1. Số ca làm lại: gấp đôi → 6.787 đ (+51,8%) [simulated] · 2. Tỉ lệ xem lại: gấp đôi → 6.292 đ (+40,7%) [simulated] · 3. Lương +25% → 5.506 đ (+23,1%) [simulated]. Giá token gấp đôi chỉ +5,6% [simulated] | Giả lập | PM trợ lý hoàn phí |
| 3 · So với nhân viên tự làm | Cả hệ thống, đã cộng 222 yêu cầu nhân viên làm thay: 5.865 đ/yêu cầu [simulated] = 0,49× [simulated] của 12.000 đ. Phạm vi noi_dia + hang_nang đã cộng chi phí cố định 40 triệu/tháng: 4.599 đ [simulated] = 0,38× [simulated] ở 45.000 yêu cầu/tháng; 5.784 đ [simulated] = 0,48× [simulated] nếu khối lượng còn một nửa. Bất lợi: xem lại 100% → 11.743 đ = 0,98× [simulated], 12.415 đ = 1,03× [simulated] nếu làm lại 15,3 phút như dữ liệu | Giả lập | PM trợ lý hoàn phí |
| 4 · Chỉ số chính, chỉ số dùng, chỉ số an toàn | Chỉ số trong đợt chạy thử: chính 82,83% (994/1.200) · dùng: bỏ qua gợi ý 27,12% (48/177) · an toàn: mở lại 7 ngày 4,25% (51/1.200; 3,97% trong phạm vi). Đợt chạy thử không có đối chứng nên chưa kết luận được tác động so với baseline 0,70 | Xong, có bằng chứng | Trưởng nhóm CSKH |
| 5 · Bảng lỗi và cách khắc phục | Hai bộ nhãn độc lập trùng 19/20 ca = 95% (lệch ca 13, thống nhất Giới hạn hệ thống). Bảng khắc phục 5 ca đủ năm loại, mỗi ca có cách phát hiện đo được (ngưỡng 0 ca hoàn sai báo "đã hoàn" mỗi giờ; 1% đơn lệch giá qua kiểm tra mẫu 100 đơn/tuần) và một vai trò phụ trách | Xong, có bằng chứng | Kỹ sư trưởng agent |
| 6 · Pilot plan | Phạm vi noi_dia (0,22× [simulated]) + hang_nang (0,69× [simulated]); loại quoc_te (1,88× [simulated], thành công 27,3%, ok theo lần chạy 30,0% → 11,4% → 2,2%) và doi_tac (0,85× [simulated], thành công 54,4%, 1,88 lần chạy/yêu cầu, điều khoản riêng). Với số cụm hiện có, chia theo nhân viên hoặc depot không đủ mẫu cho mức chênh 5 điểm (20 nhân viên mỗi nhánh tối đa 1.000 hiệu dụng; 6 depot tối đa 300). Chia theo yêu cầu cần 1.251 yêu cầu mỗi nhánh, nhưng có rủi ro ảnh hưởng giữa hai nhánh khi cùng nhân viên xử lý. Chọn chia theo nhân viên 20 + 20, ngẫu nhiên phân tầng theo depot, chấp nhận mức chênh 6 điểm. Mỗi nhánh cần 20 × 299 = 5.980 yêu cầu thực tế. Với DE = 6,96, cỡ mẫu hiệu dụng là 5.980 ÷ 6,96 ≈ 859 yêu cầu mỗi nhánh; power chỉ 0,64 nếu tác động thật là 5 điểm. Luật dừng an toàn so với đối chứng (+2 điểm) kèm trần 6%, vì mở lại hiện tại đã 4,25%; người có quyền dừng: Giám đốc vận hành | Giả lập | Giám đốc vận hành |
| 7 · Rủi ro kinh tế | Làm lại gấp đôi → 6.787 đ [simulated], theo dõi tỉ lệ làm lại > 7%/tuần (đợt thử 4,89% trong phạm vi). Xem lại 100% kéo dài → 0,98×–1,03× [simulated], hoà vốn khi mỗi lần xem lại ≤ 5,1 phút nếu làm lại 9 phút/ca, ≤ 4,8 phút nếu làm lại 15,3 phút/ca [simulated]. Khối lượng còn một nửa → chi phí cố định +2.370 đ/việc [simulated]. Chi tiết trong `chi_so.md` | Giả lập | PM trợ lý hoàn phí |

**Đề xuất: Go có điều kiện** cho pilot noi_dia + hang_nang. Con số bất lợi đã tính: power 0,64 ở mức 5 điểm; xem lại 100% đắt ngang nhân viên tự làm (0,98×–1,03× [simulated]); mở lại 7 ngày hiện tại 4,25%. Điều kiện:

- Sửa khoá chống trùng và đối soát sổ cái (lỗi hoàn hai lần ở ca 20, báo "đã hoàn" khi sổ cái lỗi 503 ở ca 7) · Kỹ sư trưởng agent · kiểm tra 2027-01-05, trước ngày bắt đầu.
- Ký chấp nhận mức chênh 6 điểm (power 0,64 nếu tác động thật là 5 điểm) · Giám đốc vận hành · 2027-01-05.
- Bật và kiểm tra đủ 10 event có trace_id ghi nhận đúng trên luồng thử · PM trợ lý hoàn phí · 2027-01-05, trước ngày bắt đầu.
- Kiểm số phút xem lại, làm lại đo thật (từ staff_review_decision, staff_rework_completed) thay cho phút simulated, tính lại chi phí mỗi việc thành công · PM trợ lý hoàn phí · 2027-01-12, sau tuần 1.
- Giảm xem lại theo bậc, chỉ giảm khi tỉ lệ sửa + bỏ < 15%. Ngưỡng hoà vốn mỗi lần xem lại: ≤ 5,1 phút nếu làm lại 9 phút/ca (giả định đề bài); ≤ 4,8 phút nếu làm lại 15,3 phút/ca (trung bình cột simulated) [simulated] · Trưởng nhóm CSKH · cuối bước rollout 0.25, 2027-01-19.
