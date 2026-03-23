import requests
import pyodbc
from datetime import datetime

# -----------------------------
# 1. API DETAILS
# -----------------------------
API_URL = "http://127.0.0.1:8000/sale"

# -----------------------------
# 2. SQL SERVER CONNECTION
# -----------------------------
conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=localhost;"
    "DATABASE=Sales_GenAI_Analytics;"
    "Trusted_Connection=yes;"
)
cursor = conn.cursor()

# -----------------------------
# 3. GET SALE DATA FROM API
# -----------------------------
sale = requests.get(API_URL).json()

# -----------------------------
# 4. MAP OR INSERT PRODUCT
# -----------------------------
cursor.execute(
    "SELECT product_id FROM dim_product WHERE product_name = ?",
    sale["product_name"]
)
row = cursor.fetchone()

if row is None:
    cursor.execute(
        "INSERT INTO dim_product (product_name) OUTPUT INSERTED.product_id VALUES (?)",
        sale["product_name"]
    )
    product_id = cursor.fetchone()[0]
    conn.commit()
else:
    product_id = row[0]

# -----------------------------
# 5. MAP OR INSERT REGION
# -----------------------------
cursor.execute(
    "SELECT region_id FROM dim_region WHERE city = ?",
    sale["city"]
)
row = cursor.fetchone()

if row is None:
    cursor.execute(
        "INSERT INTO dim_region (city) OUTPUT INSERTED.region_id VALUES (?)",
        sale["city"]
    )
    region_id = cursor.fetchone()[0]
    conn.commit()
else:
    region_id = row[0]

# -----------------------------
# 6. MAP CUSTOMER (segment-based)
# -----------------------------
cursor.execute(
    """
    SELECT TOP 1 customer_id
    FROM dim_customer
    WHERE segment = ?
    ORDER BY NEWID()
    """,
    sale["segment"]
)
row = cursor.fetchone()

if row is None:
    raise Exception(f"No customer found for segment: {sale['segment']}")

customer_id = row[0]

# -----------------------------
# 7. MAP OR INSERT CHANNEL
# -----------------------------
cursor.execute(
    """
    SELECT channel_id
    FROM dim_channel
    WHERE channel_name = ? AND platform = ?
    """,
    sale["channel"], sale["platform"]
)
row = cursor.fetchone()

if row is None:
    cursor.execute(
        """
        INSERT INTO dim_channel (channel_name, platform)
        OUTPUT INSERTED.channel_id
        VALUES (?, ?)
        """,
        sale["channel"], sale["platform"]
    )
    channel_id = cursor.fetchone()[0]
    conn.commit()
else:
    channel_id = row[0]

# -----------------------------
# 8. MAP OR INSERT PROMOTION
# -----------------------------
cursor.execute(
    "SELECT promotion_id FROM dim_promotion WHERE campaign_name = ?",
    sale["promotion"]
)
row = cursor.fetchone()

if row is None:
    cursor.execute(
        """
        INSERT INTO dim_promotion (campaign_name)
        OUTPUT INSERTED.promotion_id
        VALUES (?)
        """,
        sale["promotion"]
    )
    promotion_id = cursor.fetchone()[0]
    conn.commit()
else:
    promotion_id = row[0]

# -----------------------------
# 9. HANDLE DATE DIMENSION
# -----------------------------
sale_datetime = datetime.strptime(
    sale["sale_time"], "%Y-%m-%d %H:%M:%S"
)
date_id = int(sale_datetime.strftime("%Y%m%d"))

cursor.execute(
    "SELECT date_id FROM dim_date WHERE date_id = ?",
    date_id
)
row = cursor.fetchone()

if row is None:
    cursor.execute(
        """
        INSERT INTO dim_date
        (date_id, full_date, day_name, month_name, quarter, year, is_weekend)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        date_id,
        sale_datetime.date(),
        sale_datetime.strftime("%A"),
        sale_datetime.strftime("%B"),
        f"Q{((sale_datetime.month - 1)//3) + 1}",
        sale_datetime.year,
        1 if sale_datetime.weekday() >= 5 else 0
    )
    conn.commit()

# -----------------------------
# 10. CALCULATE PROFIT
# -----------------------------
profit = sale["revenue"] - sale["cost"]

# -----------------------------
# 11. INSERT INTO FACT TABLE
# -----------------------------
cursor.execute(
    """
    INSERT INTO fact_sales
    (
        sale_timestamp,
        date_id,
        product_id,
        customer_id,
        region_id,
        channel_id,
        promotion_id,
        quantity,
        revenue,
        cost,
        profit
    )
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """,
    sale["sale_time"],
    date_id,
    product_id,
    customer_id,
    region_id,
    channel_id,
    promotion_id,
    sale["quantity"],
    sale["revenue"],
    sale["cost"],
    profit
)

conn.commit()

# -----------------------------
# 12. CLOSE CONNECTION
# -----------------------------
cursor.close()
conn.close()

print("✅ Sale successfully inserted into fact_sales")


# to run this code use : python ingest_sales.py
