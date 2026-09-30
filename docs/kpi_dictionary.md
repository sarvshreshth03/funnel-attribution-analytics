# KPI Dictionary
One definition per metric. Dashboard and SQL views must implement these exactly.

## Volume and funnel
| KPI | Definition | Formula | Notes |
|---|---|---|---|
| Leads | Unique prospects captured | `COUNT(DISTINCT prospect_id)` | Dated by lead created date |
| Qualified Lead | Lead that reached stage 3 or higher | `max_stage_key >= 3` | Stages: 1 Captured, 2 Contacted, 3 Qualified, 4 Applied, 5 Enrolled |
| Enrollment | Lead that converted | `converted_flag = 1` | Dated by enrollment date for revenue, by created date for cohorts |
| Lead-to-Enrollment Rate | Share of leads that enrolled | `enrollments / leads` | Compare **matured cohorts** only (max lag is 60 days) |
| Stage Conversion Rate | Progress from one stage to the next | `leads reaching stage n+1 / leads reaching stage n` | "Reached" means `max_stage_key >= n` |
| Median Time to Enroll | Speed of conversion | `MEDIAN(enrollment_date - created_date)` | Enrolled leads only |

## Media efficiency
| KPI | Definition | Formula | Notes |
|---|---|---|---|
| Spend | Media cost in INR | `SUM(spend_inr)` | From `fact_spend` |
| CTR | Click-through rate | `clicks / impressions` | |
| CPC | Cost per click | `spend / clicks` | |
| CPL | Cost per lead | `spend / attributed leads` | Depends on attribution model |
| Cost per Qualified Lead | Cost of leads that reach stage 3+ | `spend / attributed qualified leads` | |
| CAC (Cost per Enrollment) | Cost to acquire one enrollment | `spend / attributed enrollments` | Primary decision metric |
| Revenue | Commission earned | `SUM(commission_inr)` for enrolled leads | Attributed revenue uses the same credit split as enrollments |
| ROAS | Return on ad spend | `attributed revenue / spend` | Below 1.0 = losing money at channel level |

## Attribution models
All models distribute **1.0 credit per enrolled lead** across that lead's touchpoints (or per lead for lead counts).
| Model | Rule |
|---|---|
| First-touch | 100% to `touch_seq = 1` |
| Last-touch | 100% to the final touch (= lead-creating source) |
| Linear | `1 / n` to each of the n touches |
| Position-based (40-20-40) | 40% first, 40% last, 20% split across middle touches; 1 touch = 100%; 2 touches = 50/50 |

## Model quality (Day 5)
| KPI | Definition |
|---|---|
| AUC | Area under ROC curve on a held-out set |
| Lift @ top decile | Conversion rate in top 10% by score / overall conversion rate |
| Capture rate @ top 30% | Share of all enrollments found in the top 30% of scored leads |
