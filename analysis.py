"""
Zudio / Apparel Retail Market Analysis — Palghar (Portfolio Demo)

IMPORTANT:
The CSV is synthetic demonstration data, not verified market research.
Do not present its numbers as actual Palghar footfall, rents, population,
competitor counts, or as proof that a store should open.
"""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

ROOT = Path(__file__).resolve().parent
DATA_PATH = ROOT / "data" / "palghar_retail_demo_data.csv"
OUTPUT_DIR = ROOT / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

def load_and_clean_data(path=DATA_PATH):
    df = pd.read_csv(path)
    df.columns = df.columns.str.strip().str.lower()
    numeric_cols = [
        "estimated_monthly_footfall", "average_spend_inr",
        "estimated_monthly_rent_inr", "nearby_apparel_competitors",
        "estimated_population", "online_interest_index"
    ]
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")
    df["month"] = pd.to_datetime(df["month"], errors="coerce")
    df = df.drop_duplicates()
    df = df.dropna(subset=["locality", "month"])
    # Median imputation keeps this demo reproducible and demonstrates cleaning.
    for col in numeric_cols:
        df[col] = df.groupby("locality")[col].transform(
            lambda s: s.fillna(s.median())
        )
        df[col] = df[col].fillna(df[col].median())
    df["estimated_monthly_sales_inr"] = (
        df["estimated_monthly_footfall"] * df["average_spend_inr"]
    )
    df["rent_to_sales_pct"] = (
        df["estimated_monthly_rent_inr"] /
        df["estimated_monthly_sales_inr"].replace(0, pd.NA) * 100
    )
    return df

def create_visualizations(df):
    sns.set_theme(style="whitegrid")
    summary = (df.groupby("locality", as_index=False)
               .agg(avg_footfall=("estimated_monthly_footfall", "mean"),
                    avg_sales=("estimated_monthly_sales_inr", "mean"),
                    monthly_rent=("estimated_monthly_rent_inr", "mean"),
                    competitors=("nearby_apparel_competitors", "mean")))
    summary = summary.sort_values("avg_sales", ascending=False)

    plt.figure(figsize=(10, 5))
    plt.bar(summary["locality"], summary["avg_sales"])
    plt.title("Illustrative Average Monthly Sales Potential by Locality")
    plt.xlabel("Locality")
    plt.ylabel("Estimated sales (INR; synthetic demo)")
    plt.xticks(rotation=25, ha="right")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "sales_potential_by_locality.png", dpi=150)
    plt.close()

    monthly = (df.groupby("month", as_index=False)
               ["estimated_monthly_sales_inr"].sum())
    plt.figure(figsize=(10, 5))
    plt.plot(monthly["month"], monthly["estimated_monthly_sales_inr"], marker="o")
    plt.title("Illustrative Monthly Sales Trend Across Localities")
    plt.xlabel("Month")
    plt.ylabel("Estimated sales (INR; synthetic demo)")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "monthly_sales_trend.png", dpi=150)
    plt.close()

    plt.figure(figsize=(8, 5))
    plt.scatter(summary["monthly_rent"], summary["avg_sales"],
                s=summary["avg_footfall"] / summary["avg_footfall"].max() * 250 + 50,
                c=summary["competitors"])
    for _, row in summary.iterrows():
        plt.annotate(row["locality"], (row["monthly_rent"], row["avg_sales"]),
                     xytext=(5, 5), textcoords="offset points", fontsize=8)
    plt.title("Rent vs Illustrative Sales Potential")
    plt.xlabel("Monthly rent (INR; synthetic demo)")
    plt.ylabel("Average monthly sales (INR; synthetic demo)")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "rent_vs_sales.png", dpi=150)
    plt.close()
    return summary

def main():
    df = load_and_clean_data()
    summary = create_visualizations(df)
    summary.to_csv(OUTPUT_DIR / "locality_summary.csv", index=False)
    print("\nDATASET CHECK")
    print(f"Rows after cleaning: {len(df)}")
    print(f"Localities analyzed: {df['locality'].nunique()}")
    print("\nLOCALITY SUMMARY (illustrative synthetic data)")
    print(summary.round(2).to_string(index=False))
    print(f"\nCharts and summary saved in: {OUTPUT_DIR}")

if __name__ == "__main__":
    main()
