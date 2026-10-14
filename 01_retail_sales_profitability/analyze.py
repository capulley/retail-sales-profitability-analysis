from pathlib import Path
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parent
DATA=ROOT/'data'
OUT=ROOT/'outputs'
OUT.mkdir(exist_ok=True)
df=pd.read_csv(DATA/'orders.csv',parse_dates=['order_date'])
df['revenue']=df.quantity*df.unit_price*(1-df.discount_rate)
df['gross_profit']=df.revenue-df.quantity*df.unit_cost
summary=df.groupby('category')[['revenue','gross_profit']].sum().sort_values('revenue',ascending=False)
summary.to_csv(OUT/'category_summary.csv')
monthly=df.groupby(df.order_date.dt.to_period('M').astype(str))['revenue'].sum()
ax=monthly.plot(kind='line',marker='o',title='Monthly revenue');ax.set_ylabel('Revenue ($)');plt.tight_layout();plt.savefig(OUT/'monthly_revenue.png');plt.close()
print(summary.round(2))
