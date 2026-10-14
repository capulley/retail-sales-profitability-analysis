# Retail Sales & Profitability Analysis

## Business question
Which product categories and regions drive revenue and gross profit, and how do sales change over time?

## Data provenance
**Synthetic demonstration data**, generated for this portfolio. These are not real customer, sales, or employer records. No results should be presented as real-world business impact.

## Run locally
```bash
python -m pip install -r requirements.txt
python analyze.py
```
The script prints key findings and saves a CSV summary and PNG chart in `outputs/`.

## Repository contents
- `data/`: sample input dataset(s)
- `analyze.py`: reproducible pandas analysis and visualization
- `sql/analysis.sql`: example SQLite-compatible analytical queries (import CSVs as same-named tables before executing)
- `outputs/`: generated artifacts

## Interview discussion prompts
Explain the business question, what each field represents, how you validated the data, which KPIs you selected, and what additional data you would need before making a real business recommendation.

## Limitations
Synthetic data does not establish causal relationships or real-world outcomes. Results are descriptive and intended to demonstrate workflow and communication.
