# Phiếu chấm hội đồng Gate 2a

Nhóm số n chấm nhóm số n + 1; nhóm cuối chấm nhóm 1. Chấm theo bằng chứng trong hồ sơ, không theo cách trình bày: một đề xuất No-go có lý do bằng số được điểm cao hơn một đề xuất Go bỏ qua con số bất lợi.

- Nhóm chấm (hội đồng): DLB
- Nhóm được chấm: PD (repo `buianhdung2kar5/K5-L3A-DAY13-PD-LaunchEconomics`, nhánh `main`)

| Tiêu chí                 | 0 điểm                            | 5 điểm                               | 10 điểm                                                                        |        Điểm | Lý do (có số)                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ------------------------ | --------------------------------- | ------------------------------------ | ------------------------------------------------------------------------------ | ----------: | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Đề xuất khớp bằng chứng  | Mâu thuẫn với số của chính nhóm   | Khớp nhưng bỏ qua một con số bất lợi | Khớp, nêu cả con số bất lợi và cách xử lý                                      |          10 | Go có điều kiện khớp số của nhóm: cả hệ thống 0,49× [simulated] đã cộng 222 ca nhân viên làm thay. Nêu đủ số bất lợi kèm cách xử lý: power 0,64 ở 5 điểm (Giám đốc vận hành ký), xem lại 100% 0,98×–1,03× [simulated] (giảm xem lại theo bậc khi sửa + bỏ < 15%), dữ liệu chạy thử chỉ có 20 staff_id ở 6 depot (điều kiện xác nhận đủ 40 người, nếu không thì 10 + 10, MDE 8 điểm). Mỗi điều kiện có vai trò và mốc kiểm tra                            |
| Số giả lập và phạm vi    | Không nhãn; phạm vi "mọi yêu cầu" | Có nhãn hoặc có thu hẹp phạm vi      | Nhãn ở mọi số giả lập; phạm vi thu hẹp có lý do bằng số                        |          10 | Phạm vi thu hẹp có lý do bằng số (noi_dia 0,22×, hang_nang 0,69×; loại quoc_te 1,88×, thành công 27,3%, và doi_tac 0,85×). Mỗi dòng, mỗi câu trả lời dùng số giả lập đều có nhãn [simulated]; các mục dựa trên cột `_simulated` ghi trạng thái Giả lập. Góp ý: nên đặt nhãn sát từng bội số, ví dụ hồ sơ mục 1 "gấp 16,3 lần", "làm lại chiếm 51,8%" và cột "So với 12.000 đ" ở A3, A4                                                                   |
| Pilot ra được quyết định | Không đối chứng hoặc thiếu cỡ mẫu | Đủ cỡ mẫu, luật dừng chung chung     | Tách được tác động, đủ mẫu, luật dừng có ngưỡng, thời hạn, người có quyền dừng |          10 | Chia theo nhân viên 20 + 20, bốc thăm có seed, phân tầng theo depot, đối chứng chạy cùng tuần; đủ mẫu cho mức chênh 6 điểm (859 hiệu dụng, 5.980 yêu cầu thực tế mỗi nhóm, DE 6,96) và ghi đánh đổi. 5 luật dừng đủ NẾU – TRONG – THÌ – KHÔNG THÌ, có ngưỡng (6%, +2 điểm, 8.000 đ, 40%), thời hạn (3 ngày, 1–2 tuần), người dừng (Giám đốc vận hành, 30 phút); luật +2 điểm chỉ từ bước 10 người. Ngày quyết định 2027-01-12 sau 7 ngày theo dõi mở lại |
| **Tổng**                 |                                   |                                      |                                                                                | **30 / 30** |                                                                                                                                                                                                                                                                                                                                                                                                                                                          |

**Quyết định của hội đồng:** Go có điều kiện

**Lý do:** Phạm vi noi_dia + hang_nang rẻ hơn nhân viên tự làm (0,49× cả hệ thống; 0,38× trong phạm vi đã cộng cố định [simulated]) và kế hoạch pilot tách được tác động. Các điều kiện của nhóm là đúng chỗ cần chặn: hai lỗi tiền (hoàn trùng ca 20, hoàn thừa ngầm ca 5), xác nhận đủ 40 nhân viên, chấp nhận power 0,64. Góp ý nhỏ: đặt nhãn [simulated] sát từng bội số, và hồ sơ mục 4 ghi "8 event" trong khi `chi_so.md` liệt kê 10 event.

**Một câu hỏi cho đội trình:** Nếu ngày 07/12 Giám đốc vận hành chỉ xác nhận được 20 nhân viên, nhóm chia 10 + 10 dưới 20 cụm với MDE 8 điểm: khi đó pilot còn ra được quyết định không, hay nhóm sẽ đổi đề xuất thành No-go?

**Câu trả lời của đội trình (ghi lại tại buổi):**

Với 10 + 10, pilot không còn ra được quyết định, nên nhóm đổi đề xuất thành No-go cho thiết kế này. Đây là No-go cho kế hoạch pilot hiện tại, không phải kết luận rằng trợ lý không đáng làm.

Lý do bằng số (ICC 0,02, khoảng 30,7 yêu cầu/người/ngày trong phạm vi):

| | 10 + 10, m = 299 (khoảng 10 ngày) | 10 + 10, m = 796 (khoảng 26 ngày) |
| --- | ---: | ---: |
| Cỡ mẫu hiệu dụng mỗi nhóm | khoảng 430 | khoảng 471 |
| Power nếu tác động thật là 5 điểm | 0,38 | 0,41 |
| Power nếu tác động thật là 6 điểm | 0,51 | 0,55 |
| Power nếu tác động thật là 8 điểm | 0,76 | 0,80 |

- Kéo dài thời gian gần như không giúp được. Cỡ mẫu hiệu dụng bị chặn dưới 10 ÷ 0,02 = 500, dù mỗi người làm bao nhiêu đơn. Chạy gấp 2,6 lần thời gian, power ở mức 6 điểm chỉ tăng từ 0,51 lên 0,55.
- Chỉ phát hiện được mức chênh 8 điểm, tức 70% → 78%. Nếu trợ lý thật sự giúp 5–6 điểm, khả năng pilot thấy được chỉ khoảng một nửa hoặc thấp hơn. Kết quả "không thấy khác biệt" khi đó gần như không cho biết gì.
- Câu 5 của D2 không đạt: chỉ có 10 cụm, dưới mức 20. Với ít cụm như vậy, phép kiểm định kém tin cậy hơn nữa.
- Trong hồ sơ, việc xác nhận đủ 40 nhân viên là một điều kiện viết trước của đề xuất Go có điều kiện. Điều kiện không đạt thì giữ chữ "Go" sẽ mâu thuẫn với chính bằng chứng của nhóm.

Việc phải làm để quay lại cổng:

- Mở rộng sang đủ 40 nhân viên ở cả 12 depot để chia 20 + 20 như kế hoạch: MDE 6 điểm, power 0,64 ở mức 5 điểm. Phụ trách: Giám đốc vận hành.
- Nếu không mở rộng được, chỉ xin chạy thử vận hành an toàn: 10 nhân viên, chỉ theo dõi luật dừng an toàn và chi phí (hoàn trùng, mở lại dưới 6%, chi phí biến đổi dưới 8.000 đ). Phải ghi rõ đợt này không kết luận được tác động lên chỉ số chính. Đây là một kế hoạch khác và phải trình lại Gate 2a.
- Trong lúc chờ, vẫn làm các việc không phụ thuộc cỡ mẫu: khoá chống trùng, đối soát sổ cái, đo phút xem lại thật thay cho số giả lập.

Câu chốt khi trình: "Thà No-go có số còn hơn chạy một pilot chỉ có khoảng 50% cơ hội thấy tác động thật rồi đem ra quyết định."
