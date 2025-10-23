import pandas as pd
import matplotlib.pyplot as plt
import os
os.makedirs('visuals', exist_ok=True)
df = pd.read_csv('data/usage_2024.csv', parse_dates=['TripDate'])
df['Month'] = df['TripDate'].dt.to_period('M').astype(str)
avg_cost_trip = df['Cost'].mean() if len(df) else 0
cost_per_km = (df['Cost'].sum() / df['KM'].sum()) if df['KM'].sum() else 0
monthly_spend = df.groupby('Month')['Cost'].sum()
with open('visuals/kpi_summary.txt','w') as f:
    f.write(f'Average Cost per Trip: ${avg_cost_trip:.2f}\n')
    f.write(f'Cost per KM: ${cost_per_km:.2f}\n')
plt.figure(); monthly_spend.plot(marker='o'); plt.title('407 ETR Monthly Cost Trend (2024)'); plt.xlabel('Month'); plt.ylabel('Total Cost ($)'); plt.tight_layout(); plt.savefig('visuals/monthly_cost_trend.png'); plt.close()
plt.figure(); plt.scatter(df['KM'], df['Cost']); plt.title('KM vs Cost per Trip (2024)'); plt.xlabel('KM'); plt.ylabel('Cost ($)'); plt.tight_layout(); plt.savefig('visuals/km_vs_cost.png'); plt.close()
plt.figure(); df['VehicleClass'].value_counts().plot(kind='bar'); plt.title('Trips by Vehicle Class (2024)'); plt.ylabel('Trips'); plt.tight_layout(); plt.savefig('visuals/class_trips_bar.png'); plt.close()
print('Done')