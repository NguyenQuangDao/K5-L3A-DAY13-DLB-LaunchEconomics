# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

**Nhóm:** DLB  
**Người phụ trách:** Nguyễn Gia Bảo - 2A202603647 (Đặc tả), Nguyễn Quang Đạo - 2A202603614 (Kiểm số)

Nguồn số: E1 do `python lab13.py` in ra (hàm `chi_so_e1`); số rủi ro lấy từ B1, B4, A4 trong `lab13.py` và `bang_chi_phi.md`. Mọi số tính từ cột `_simulated` ghi nhãn [simulated].

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h` bằng 1 và `mo_lai_trong_7_ngay` bằng 0, chia tổng số yêu cầu | 82,83% (994/1.200) |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu được xem lại | 27,12% (48/177) |
| An toàn | Tỉ lệ lỗi lọt đến khách | `mo_lai_trong_7_ngay` bằng 1, chia tổng số yêu cầu | 4,25% (51/1.200); 3,97% trong phạm vi noi_dia + hang_nang |
| Dùng | Nhóm tự đề xuất: % yêu cầu của nhóm dùng trợ lý được xử lý qua trợ lý | Số yêu cầu `arm = tro_ly` có `agent_suggestion_shown`, chia số yêu cầu `arm = tro_ly` | Không cần tính |
| An toàn | Nhóm tự đề xuất: % đơn hoàn sai tiền qua kiểm tra mẫu hằng tuần (bắt lỗi ngầm như ca 5, 17) | Số đơn `audit_sample_checked` có `so_tien_da_hoan` khác `so_tien_dung`, chia số đơn được kiểm tra trong tuần | Không cần tính |

Chỉ số chính trong đợt chạy thử là 82,83%. Đợt chạy thử không có nhóm đối chứng, nên chưa kết luận được tác động của trợ lý so với baseline 0,70; pilot có đối chứng sẽ trả lời câu này.

Ngưỡng an toàn của pilot đặt sau khi nhìn tỉ lệ hiện tại: mở lại 7 ngày trong phạm vi đã là 3,97%, nên ngưỡng tuyệt đối 3% sẽ dừng pilot ngay tuần đầu. Pilot dùng mức chênh +2 điểm phần trăm so với nhóm đối chứng, kèm trần tuyệt đối 6% (luật dừng trong `pilot_plan.yaml`).

## Danh sách event

Mỗi event có `trace_id` để nối với trace của agent.

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| refund_request_created | App khách | request_id, loai, so_tien, depot, staff_id, arm, trace_id | Khi khách gửi yêu cầu |
| input_validation_failed | Agent | truong_loi, gia_tri_nhap, loai_loi, trace_id | Khi đầu vào của khách không hợp lệ (vd mã đơn sàn TMĐT thay vì mã vận đơn) |
| agent_run_completed | Agent | attempt, tokens_in, tokens_out, tool_calls, status, trace_id | Sau mỗi lần chạy, kể cả lần lỗi |
| agent_suggestion_shown | Giao diện nhân viên | staff_id, so_tien_de_xuat, trace_id | Khi gợi ý hiện ra cho nhân viên |
| staff_review_decision | Nhân viên | quyet_dinh (giu, sua, bo), phut_xem_lai đo thật, trace_id | Khi bấm gửi, sửa hoặc bỏ |
| staff_rework_completed | Nhân viên | phut_lam_lai đo thật, ly_do, trace_id | Khi làm lại xong |
| refund_ledger_write | Dịch vụ sổ cái | idempotency_key, so_tien, ket_qua, trace_id | Khi ghi sổ hoàn tiền |
| handoff_to_staff | Agent | reason, tom_tat, trace_id | Khi chuyển cho nhân viên |
| ticket_closed | Hệ thống ticket | closed_at, trace_id | Khi đóng yêu cầu |
| ticket_reopened | Khách | reopened_at, reason, trace_id | Khi khách mở lại |
| audit_sample_checked | Kế toán | so_tien_da_hoan, so_tien_dung, bang_gia_version, trace_id | Hằng tuần, mẫu 100 đơn |

**Kiểm tra chéo:** mỗi chỉ số tính được từ các event trên.

- Chính: `refund_request_created` (mẫu số, thời điểm tạo) + `ticket_closed` (đóng trong 24 giờ) + `ticket_reopened` (mở lại trong 7 ngày).
- Dùng, bỏ qua gợi ý: `staff_review_decision` (sua, bo trên tổng quyết định); `agent_suggestion_shown` xác nhận gợi ý đã hiện.
- An toàn, mở lại 7 ngày: `ticket_reopened` chia `refund_request_created`.
- Dùng, tự đề xuất: `agent_suggestion_shown` chia `refund_request_created` có `arm = tro_ly`.
- An toàn, tự đề xuất: `audit_sample_checked`.
- Chi phí mỗi việc thành công (luật dừng chi phí): `agent_run_completed` (token, tool), `staff_review_decision` (phút xem lại), `staff_rework_completed` (phút làm lại), `ticket_closed` và `ticket_reopened` (đếm việc thành công).
- Luật dừng hoàn trùng: `refund_ledger_write` (idempotency_key ghi sổ hai lần). Tỉ lệ chuyển nhân viên: `handoff_to_staff`. Lỗi do người dùng (ca 9): `input_validation_failed`.

## E2 · Rủi ro kinh tế

Số lấy từ bảng độ nhạy và B4, A4 trong `bang_chi_phi.md`.

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại tăng gấp đôi | Chi phí mỗi việc thành công lên 6.787 đ [simulated], +51,8% [simulated] | Tỉ lệ làm lại theo tuần > 7% (đợt thử 4,89% trong phạm vi), từ `staff_rework_completed` | Rà 20 trace làm lại, đặt giới hạn 2 lần chạy trong 5 ngày làm việc; nếu không giảm thì thu hẹp về noi_dia | PM trợ lý hoàn phí |
| Phải xem lại 100% kéo dài | 11.743 đ [simulated] = 0,98× [simulated] nếu làm lại 9 phút/ca; 12.415 đ [simulated] = 1,03× [simulated] nếu làm lại 15,3 phút/ca [simulated] như dữ liệu | % yêu cầu được xem lại còn > 50% cuối bước rollout 0.25 (2027-01-19), từ `staff_review_decision` | Giảm xem lại theo bậc khi tỉ lệ sửa + bỏ < 15%; mỗi lần xem lại phải ≤ 5,1 phút [simulated] (làm lại 9 phút/ca) hoặc ≤ 4,8 phút [simulated] (làm lại 15,3 phút/ca) | Trưởng nhóm CSKH |
| Khối lượng thấp hơn dự kiến | Chi phí cố định 40 triệu/tháng: +1.185 đ/việc ở 45.000 yêu cầu/tháng, +2.370 đ/việc nếu còn một nửa; chi phí mỗi việc thành công trong phạm vi tăng từ 4.599 đ [simulated] lên 5.784 đ [simulated] | Số việc thành công theo tuần < 50% kế hoạch | Không mở rộng pilot; xem lại hợp đồng chi phí cố định | PM trợ lý hoàn phí |
| Pilot chỉ đủ mẫu cho mức chênh 6 điểm | Power 0,64 nếu tác động thật là 5 điểm: khoảng 36% khả năng không thấy được tác động có thật | Tại ngày đọc kết quả 2027-02-03, chênh lệch quan sát dưới 6 điểm và không có ý nghĩa thống kê | Ký chấp nhận đánh đổi trước 2027-01-05; khi đọc kết quả ghi rõ "chưa thấy chênh 6 điểm" không có nghĩa là "không có tác động", quyết định thêm dựa trên chi phí và chỉ số an toàn | Giám đốc vận hành |

Ghi chú:

- Khi xem lại 100%, tiền xem lại chiếm 89,7% [simulated] tổng chi phí (9.480.000 đ ÷ 10.568.513 đ [simulated]), nên trợ lý gần như không tiết kiệm được gì.
- Chia theo nhân viên 20 + 20: mỗi nhánh cần 20 × 299 = 5.980 yêu cầu thực tế; với DE = 6,96, cỡ mẫu hiệu dụng là 5.980 ÷ 6,96 ≈ 859 yêu cầu mỗi nhánh.

## Kết luận

- Chỉ số trong đợt chạy thử: chính 82,83%, dùng (bỏ qua gợi ý) 27,12%, an toàn (mở lại 7 ngày) 4,25%. Chưa có đối chứng nên chưa kết luận về tác động.
- Hai rủi ro kinh tế lớn nhất là số ca làm lại (+51,8% [simulated] khi gấp đôi) và tỉ lệ xem lại (+40,7% [simulated] khi gấp đôi); pilot phải theo dõi cả hai theo tuần.
- So với nhân viên tự làm, chi phí cả hệ thống là 5.865 đ/yêu cầu [simulated] = 0,49× [simulated] của 12.000 đ. Con số 4.472 đ [simulated] chỉ chia cho việc trợ lý làm xong, chưa tính 222 yêu cầu nhân viên làm thay.
