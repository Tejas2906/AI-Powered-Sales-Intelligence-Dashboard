import pyodbc
from datetime import datetime

conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=localhost;"
    "DATABASE=Sales_GenAI_Analytics;"
    "Trusted_Connection=yes;"
)
cursor = conn.cursor()

# -----------------------------
# OVERALL PERFORMANCE
# -----------------------------

cursor.execute("SELECT SUM(revenue), SUM(profit) FROM fact_sales")
revenue, profit = cursor.fetchone()

profit_margin = (profit / revenue) * 100 if revenue else 0

# Month-over-Month Growth
cursor.execute("""
SELECT 
    SUM(CASE WHEN MONTH(sale_timestamp)=MONTH(GETDATE()) 
             THEN revenue ELSE 0 END),
    SUM(CASE WHEN MONTH(sale_timestamp)=MONTH(DATEADD(MONTH,-1,GETDATE())) 
             THEN revenue ELSE 0 END)
FROM fact_sales
""")

current_month, prev_month = cursor.fetchone()
mom_growth = ((current_month - prev_month) / prev_month * 100) if prev_month else 0

# Top State
cursor.execute("""
SELECT TOP 1 dr.state, SUM(fs.revenue)
FROM fact_sales fs
JOIN dim_region dr ON fs.region_id = dr.region_id
GROUP BY dr.state
ORDER BY SUM(fs.revenue) DESC
""")
top_state = cursor.fetchone()[0]

# Top Category
cursor.execute("""
SELECT TOP 1 dp.category, SUM(fs.revenue)
FROM fact_sales fs
JOIN dim_product dp ON fs.product_id = dp.product_id
GROUP BY dp.category
ORDER BY SUM(fs.revenue) DESC
""")
top_category = cursor.fetchone()[0]

# Best Channel
cursor.execute("""
SELECT TOP 1 dc.channel_name, SUM(fs.revenue)
FROM fact_sales fs
JOIN dim_channel dc ON fs.channel_id = dc.channel_id
GROUP BY dc.channel_name
ORDER BY SUM(fs.revenue) DESC
""")
top_channel = cursor.fetchone()[0]

# Lowest Margin Category
cursor.execute("""
SELECT TOP 1 dp.category,
SUM(fs.profit) * 100.0 / SUM(fs.revenue)
FROM fact_sales fs
JOIN dim_product dp ON fs.product_id = dp.product_id
GROUP BY dp.category
ORDER BY SUM(fs.profit) * 100.0 / SUM(fs.revenue) ASC
""")
low_margin_category = cursor.fetchone()[0]

# Lowest Profit State
cursor.execute("""
SELECT TOP 1 dr.state, SUM(fs.profit)
FROM fact_sales fs
JOIN dim_region dr ON fs.region_id = dr.region_id
GROUP BY dr.state
ORDER BY SUM(fs.profit) ASC
""")
low_profit_state = cursor.fetchone()[0]

risk_score = 0

if profit_margin < 12:
    risk_score += 1

if mom_growth < 0:
    risk_score += 1

if risk_score == 0:
    risk_level = "Low Risk"
elif risk_score == 1:
    risk_level = "Moderate Risk"
else:
    risk_level = "High Risk"

performance_overview = f"""
The business generated total revenue of ₹{revenue:,.0f} with a profit margin of {profit_margin:.2f}%. 
Month-over-Month growth stands at {mom_growth:.2f}%, indicating {'positive momentum' if mom_growth > 0 else 'performance pressure'}.
Overall business risk level is classified as {risk_level}.
"""

growth_drivers = f"""
Revenue performance is primarily driven by {top_state}, with {top_category} emerging as the leading category.
The {top_channel} channel continues to contribute significantly to overall sales growth.
"""

risk_areas = f"""
Margin pressure is observed in the {low_margin_category} category.
Additionally, profitability remains weak in {low_profit_state}, requiring operational and pricing review.
"""

recommendations = f"""
1. Optimize pricing and cost structure in low-margin categories.
2. Increase strategic investment in high-performing regions and channels.
3. Monitor month-over-month growth closely to ensure sustained momentum.
"""
cursor.execute("""
INSERT INTO ai_summary
(performance_overview, growth_drivers, risk_areas, recommendations, risk_score)
VALUES (?, ?, ?, ?, ?)
""",
performance_overview,
growth_drivers,
risk_areas,
recommendations,
risk_score
)

conn.commit()
cursor.close()
conn.close()

print("✅ Hybrid Executive Intelligence Summary Generated Successfully")

# To run this script, use the command: python generate_executive_engine.py
