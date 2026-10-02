import os
import argparse
import pandas as pd
import oracledb

def patch():
    dsn = "localhost:1521/FREEPDB1"
    user = "funnel_prj"
    pwd = os.environ.get("FUNNEL_DB_PASSWORD", "Funnel_Pass1")
    csv_path = "../data/raw/Leads.csv"

    print(f"Reading {csv_path}...")
    df = pd.read_csv(csv_path)

    # Use Lead Number as join key to avoid any UUID string mismatch
    df_clean = df[["Lead Number", "Total Time Spent on Website"]].dropna(subset=["Lead Number"]).copy()
    df_clean["time_sec"] = pd.to_numeric(df_clean["Total Time Spent on Website"], errors="coerce").fillna(0).astype(int)
    df_clean["lead_num"] = df_clean["Lead Number"].astype(int)

    data = [(int(r["time_sec"]), int(r["lead_num"])) for _, r in df_clean.iterrows()]
    print(f"Ready to update {len(data):,} records...")

    conn = oracledb.connect(user=user, password=pwd, dsn=dsn)
    cur = conn.cursor()

    cur.executemany("""
        UPDATE fact_leads
        SET time_on_site_sec = :1
        WHERE lead_number = :2
    """, data)

    conn.commit()
    print(f"Done! Rows updated: {cur.rowcount}")
    cur.close()
    conn.close()

if __name__ == "__main__":
    patch()