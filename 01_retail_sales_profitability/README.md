# Retail Sales & Profitability Analysis

## Project Overview

This project focuses on analyzing retail sales data to better understand revenue, profitability, and overall business performance. The goal was to identify which product categories generate the most revenue, compare profitability across categories, and examine sales trends over time.

I used Python and SQL to approach the dataset from a business analytics perspective, focusing on how data can support better business decisions.

## Tools & Technologies

- **Python:** Data analysis and calculations
- **pandas:** Data manipulation and aggregation
- **Matplotlib:** Data visualization
- **SQL:** Revenue, profitability, and regional analysis
- **CSV:** Data storage and reporting

## Business Questions

1. Which product categories generate the most revenue?
2. Which categories contribute the most gross profit?
3. How does revenue change over time?
4. How can sales data help identify opportunities for improving business performance?

## Methodology

I started by importing the sales dataset into Python using pandas. I calculated revenue and gross profit using quantities, product prices, discounts, and unit costs.

I then grouped the data by product category to compare financial performance. I also analyzed monthly revenue trends and created a line chart to visualize changes over time.

Additionally, I included SQL queries to demonstrate how similar business questions can be answered directly through a database.

## Key Findings

The analysis produced the following results:

| Product Category | Total Revenue | Gross Profit |
|---|---:|---:|
| Electronics | $249,420.45 | $81,985.49 |
| Home | $133,679.08 | $45,447.13 |
| Apparel | $80,252.32 | $26,773.92 |
| Office | $43,725.06 | $15,046.49 |

**Electronics was the strongest-performing category**, generating the highest revenue and total gross profit.

Home products ranked second, while Apparel and Office contributed smaller portions of overall sales.

These findings demonstrate how category-level analysis can help businesses understand where their revenue and profit are coming from.

## Business Recommendations

Based on these findings, I would recommend:

- **Prioritize high-performing categories:** Investigate opportunities to expand or promote Electronics products, given their strong revenue contribution.
- **Evaluate lower-performing categories:** Review pricing, demand, and product selection in Apparel and Office to identify potential improvements.
- **Monitor monthly sales trends:** Track revenue consistently to identify seasonal patterns or unexpected changes.
- **Expand profitability analysis:** Incorporate additional expenses and customer-level data to better understand actual business profitability.

These are potential recommendations based on the simulated data, not changes implemented by a real business.

## Project Files

- `data/orders.csv` — Retail transaction dataset
- `analyze.py` — Python analysis and visualization script
- `sql/analysis.sql` — SQL queries for sales and profitability analysis
- `outputs/category_summary.csv` — Category-level revenue and gross profit results
- `outputs/monthly_revenue.png` — Monthly revenue visualization
- `requirements.txt` — Required Python libraries

## How to Run

Install the required libraries:

```bash
python -m pip install -r requirements.txt
```

Run the analysis:

```bash
python analyze.py
```

The script generates a category-level summary and monthly revenue chart in the `outputs` folder.

## Dataset Disclaimer

This project uses **synthetically generated retail sales data** for educational and portfolio purposes. It does not contain actual customer information or represent the financial performance of a real company.

## What I Learned

This project helped me practice taking raw transactional data and turning it into useful business information. I gained experience calculating financial metrics, organizing datasets, writing analytical SQL queries, and creating visualizations.

More importantly, it reinforced the importance of looking beyond the numbers and considering how analytical findings can support business decisions.
