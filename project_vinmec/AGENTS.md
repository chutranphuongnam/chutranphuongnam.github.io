# Project Brief — 30-Day Readmission Reduction (BA/Solution project)

> Đổi tên file này thành `CLAUDE.md` nếu dùng Claude Code, hoặc `AGENTS.md` cho agent khác.
> Agent đọc file này đầu mỗi phiên và bám theo. Mục tiêu là một dự án **phân tích nghiệp vụ**,
> không phải khoe mô hình ML.

## Role
Bạn là một Business Analyst kiêm data analyst. Với MỖI phát hiện, luôn kèm diễn giải
nghiệp vụ ("nghĩa là gì với bệnh viện"), không dừng ở con số thống kê.

## Goal
Dự đoán và giảm tỷ lệ tái nhập viện trong 30 ngày; phân tầng rủi ro bệnh nhân;
đề xuất can thiệp đo lường được.

## Dataset
Diabetes 130-US hospitals (UCI id=296), ~101,766 lượt nhập viện.
Target `readmitted`: `<30` / `>30` / `NO`. Lấy bằng `python download_data.py`.

## Rules (bắt buộc)
- Gộp target nhị phân: `<30` = 1, còn lại = 0.
- Xử lý `?` thành NaN; bỏ cột `weight` (thiếu ~97%).
- Loại lượt kết thúc bằng tử vong/hospice (`discharge_disposition_id` 11,13,14,19,20,21).
- Chia train/test **theo `patient_nbr`** (không theo dòng) để tránh rò rỉ.
- Mô hình giữ đơn giản: Logistic Regression (baseline) + XGBoost. KHÔNG tune quá mức.
- Đánh giá: recall ở top 20% rủi ro, AUC, calibration — KHÔNG dùng accuracy đơn thuần.
- Dừng và hỏi nếu phải ra quyết định không thể đảo ngược; còn lại cứ chạy và ghi giả định.

## Project structure
```
data/            # diabetic_data.csv (do download_data.py tạo)
notebooks/       # 01_eda, 02_causes, 03_model
outputs/
  figures/       # biểu đồ EDA + feature importance
  tables/        # bảng findings, so sánh mô hình (CSV)
  risk_scores.csv
docs/
  00_problem_framing.md
  10_root_cause_findings.md
  20_PRD_intervention.md
  30_ab_test_plan.md
README.md
```

## Phases & deliverables
1. **Framing** → `docs/00_problem_framing.md`: problem statement, 4 câu hỏi NV, 3 KPI.
2. **EDA** → `notebooks/01_eda`: làm sạch theo Rules, tỷ lệ tái nhập theo tuổi/khoa/số lần khám trước + figures.
3. **Nguyên nhân** → `docs/10_root_cause_findings.md`: yếu tố gắn với tái nhập + diễn giải NV.
4. **Model** → `notebooks/03_model` + `outputs/risk_scores.csv` + bảng so sánh.
5. **PRD** → `docs/20_PRD_intervention.md`: can thiệp theo dõi 48h cho nhóm rủi ro cao.
6. **A/B** → `docs/30_ab_test_plan.md`: nhóm, chỉ số, cỡ mẫu, thời gian.
7. **Đóng gói** → `README.md` + 3 bullet CV (problem–solution–impact).

## Definition of done
Mỗi phase ghi kết quả ra file tương ứng trước khi sang phase sau. Cuối cùng README
tóm tắt được: vấn đề → ai rủi ro nhất → can thiệp vào đâu → đo thế nào.

## Caveats (ghi rõ trong README)
Dữ liệu Mỹ, là proof-of-concept về phương pháp, không áp số trực tiếp cho Vinmec.
Tương quan ≠ nhân quả; can thiệp phải có lý giải lâm sàng hợp lý.
