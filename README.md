# Lead-to-Enrollment Funnel & Marketing Attribution Analytics

End-to-end analytics project for an online-education lead-gen business: warehouse design, ETL with
data-quality checks, funnel and cohort analysis, multi-touch attribution, budget reallocation, lead scoring
and a dashboard. **Spend, campaigns and touchpoint journeys are simulated** (see `docs/BRD.md` section 7).

## Quick start
```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
# 1. download the Kaggle "Lead Scoring" Leads.csv into data/raw/
# 2. generate the synthetic source extracts (seeded, reproducible)
python src/generate_synthetic.py
```
Oracle setup: run `sql/00_create_user.sql` as SYSTEM, then `sql/01_schema_oracle.sql` as FUNNEL.

## Structure
```
config/   channel_mapping.csv, campaigns.csv   (single source of truth for mappings and cost assumptions)
data/     raw/ (Kaggle file, git-ignored) · synthetic/ (generated, git-ignored)
docs/     BRD.md, kpi_dictionary.md
sql/      DDL, later: KPI views
src/      generate_synthetic.py, later: etl, attribution, model, dashboard
```

## Build log
- [x] Day 1: scope, KPI dictionary, star schema, synthetic data generator
- [ ] Day 2: warehouse load + ETL + data-quality checks
- [ ] Day 3: KPI views, funnel, cohorts
- [ ] Day 4: attribution + budget reallocation
- [ ] Day 5: lead-scoring model
- [ ] Day 6: dashboard
- [ ] Day 7: memo, README polish, GitHub release
