# Palghar Apparel Retail Market Analysis (Portfolio Demo)

## Project objective
Demonstrate a Data Analyst workflow for comparing retail localities in Palghar:
data cleaning, exploratory analysis, visualizations, SQL analysis, and business interpretation.

> **Data transparency:** The included CSV is **synthetic demonstration data** created for this portfolio project. It is not collected field data and does not represent verified Palghar footfall, rent, population, competitor counts, customer spending, or actual Zudio performance. The results are practice outputs only and cannot establish whether a store should open.

## Tools
- Python
- Pandas and NumPy
- Matplotlib and Seaborn
- SQL (SQLite-compatible queries)

## Repository structure
```text
zudio_palghar_market_analysis/
├── data/
│   └── palghar_retail_demo_data.csv
├── outputs/                  # Generated when the script runs
├── sql/
│   └── analysis_queries.sql
├── analysis.py
├── requirements.txt
└── README.md
```

## Run locally
1. Install Python 3.10 or newer.
2. Clone/download this repository and open a terminal in the project folder.
3. Create and activate a virtual environment (optional but recommended):
   - Windows: `python -m venv .venv` then `.venv\\Scripts\\activate`
   - macOS/Linux: `python3 -m venv .venv` then `source .venv/bin/activate`
4. Install dependencies:
   `pip install -r requirements.txt`
5. Run:
   `python analysis.py`

The script cleans the CSV, calculates illustrative sales potential (footfall × average spend), and saves charts plus a locality summary in `outputs/`.

## SQL
Open `sql/analysis_queries.sql` in SQLite, DB Browser for SQLite, or adapt it to your SQL platform. The script assumes the CSV has been imported as a table named `palghar_retail_demo_data`.

## Analysis workflow
1. Inspect column types and missing values.
2. Remove duplicate rows and invalid date/locality records.
3. Convert numeric columns and impute missing numeric values using locality medians.
4. Create an illustrative sales proxy: estimated monthly footfall × average spend.
5. Compare localities on sales proxy, rent, competitor count, and footfall.
6. Visualize locality comparisons and monthly trends.

## How to discuss it in an interview
"I built a retail market-analysis demo to practice an end-to-end Data Analyst workflow. I used Pandas to clean missing values and duplicates, created a sales proxy from footfall and average spend, and used Seaborn/Matplotlib to compare localities and trends. I also wrote SQL queries for aggregation and ranking. The dataset is synthetic, so I would validate the assumptions with primary research and reliable public data before making a real site-selection recommendation."

## Important next step for a real business recommendation
Replace the demo CSV with verified data such as actual store footfall, rent quotations, competitor locations, local population data, and customer surveys. Document sources, dates, and assumptions before making conclusions.
