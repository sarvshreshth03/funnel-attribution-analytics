# Business Requirements Document
**Project:** Lead-to-Enrollment Funnel & Marketing Attribution Analytics
**Author:** Shreshth · **Version:** 0.1 (Day 1) · **Status:** Draft

## 1. Background
An online-education lead-generation platform (fictional) acquires prospective students through paid
(Google, Meta, Microsoft, YouTube), organic, direct and referral channels, then routes them through a
sales funnel to enrollment at partner universities. The platform earns a **commission per enrollment**.
Marketing currently judges channels by **last-touch cost per lead**, which ignores (a) lead quality and
(b) the channels that introduced the prospect earlier in the journey.

## 2. Business problem
Budget is allocated using cost per lead, but cost per lead does not equal cost per *enrollment*.
Channels that open journeys (Meta, YouTube) look expensive under last-touch and risk being cut,
while channels that close journeys (Direct, Chat, Brand search) look cheap and over-credited.

## 3. Objectives
1. Build a trusted, documented view of the funnel from lead capture to enrollment.
2. Quantify how much channel performance depends on the **attribution model** used.
3. Identify where the next rupee of budget should go, using cost per enrollment and ROAS.
4. Rank leads by conversion probability so sales effort goes where it pays back.

## 4. Stakeholders (fictional)
| Role | Interest |
|---|---|
| Head of Marketing | Budget split across channels and campaigns |
| Performance Marketing Lead | Campaign-level CAC / ROAS, what to pause or scale |
| Sales / Counselling Head | Lead prioritisation, funnel drop-off |
| Finance | Commission revenue vs spend, forecast accuracy |

## 5. Business questions (mapped to build days)
| # | Question | Day |
|---|---|---|
| Q1 | Where do leads drop off in the funnel, by channel and course? | 3 |
| Q2 | How does lead-to-enrollment conversion vary by acquisition week (cohorts)? | 3 |
| Q3 | Which campaigns produce the cheapest *enrollment*, not the cheapest lead? | 3-4 |
| Q4 | How much do channel rankings change between first-touch, last-touch, linear and position-based attribution? | 4 |
| Q5 | If budget moves from the worst to the best channel, what is the estimated impact? | 4 |
| Q6 | Which leads should sales call first (top-decile lift)? | 5 |

## 5a. Success criteria
- All KPIs defined once in `kpi_dictionary.md` and implemented as SQL views (no metric logic in the dashboard).
- Data-quality checks catch 100% of the defects listed in `_injection_log.json`.
- Attribution comparison shows a clear, explainable shift in at least two channels' cost per enrollment.
- Lead-scoring model beats a naive baseline with a lift of at least 2x in the top decile.
- Every finding in the memo has a recommendation and an estimated impact.

## 6. Scope
**In scope:** star-schema warehouse (Oracle), Python ETL with data-quality checks, funnel and cohort
analysis, 4 attribution models, budget reallocation scenario, lead-scoring model, Streamlit dashboard, insights memo.
**Out of scope:** real-time pipelines, creative/ad-copy analysis, incrementality or geo experiments,
CRM integration, any confidential employer data.

## 7. Data sources and honesty about synthetic data
| Data | Source | Real or simulated |
|---|---|---|
| Lead behaviour, specialization, lead source, converted flag | Kaggle Lead Scoring dataset | **Real** |
| Lead created date, funnel stage reached, enrollment date, commission | Generated (seeded) | Simulated |
| Campaigns, ad spend, impressions, clicks | Generated from config assumptions | Simulated |
| Earlier touchpoints in each journey | Generated (Kaggle lead source = last touch) | Simulated |

All simulated assumptions live in `config/` and `src/generate_synthetic.py` and are reproducible via a seed.
The README states plainly that spend, campaigns and journeys are simulated; conclusions demonstrate the
*method*, not real-world channel performance.

## 8. Assumptions and limitations
- Kaggle "Lead Source" is treated as the last (lead-creating) touch; earlier touches are simulated.
- Commission per enrollment varies by specialization (INR 12k-18k) with random noise.
- Attribution is rules-based (no data-driven / Shapley model) and observational, so it does not prove causation.
- Cost per click and click-to-touch rates are assumptions; absolute CAC/ROAS values are illustrative.

## 9. Deliverables
Warehouse DDL and ETL code, KPI SQL views, analysis notebooks/scripts, lead-scoring model,
Streamlit dashboard, one-page insights memo, README with architecture diagram.
