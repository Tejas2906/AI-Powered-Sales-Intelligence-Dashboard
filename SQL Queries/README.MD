
## 🏗️ System Architecture

The **AI-Powered Sales Intelligence Dashboard** is designed as a **complete end-to-end data pipeline** that transforms raw sales data into actionable business insights using **Data Engineering, Data Warehousing, Business Intelligence, and Generative AI**.

The architecture follows a **Star Schema (as implemented in the Power BI Model View)** where a central fact table connects with multiple dimension tables, enabling scalable and high-performance analytics.

---

## 🔄 End-to-End Pipeline Flow

# 🧩 System Architecture (Block Diagram)

```text
+----------------------+
|      Sales API       |
+----------+-----------+
           |
           v
+-------------------------------+
| Data Ingestion Pipeline       |
| (Python Scripts)              |
+----------+--------------------+
           |
           v
+-------------------------------+
| Data Cleaning & Transformation|
+----------+--------------------+
           |
           v
+-------------------------------+
| Data Warehouse (Star Schema)  |
| fact_sales + dimension tables |
+----------+--------------------+
           |
           v
+-------------------------------+
| AI Summary Table Generation   |
+----------+--------------------+
           |
           v
+-------------------------------+
| Power BI Dashboard            |
| (Model View + Visuals)        |
+----------+--------------------+
           |
           v
+----------------------+
|   Business Insights  |
+----------------------+

```
---

## 📡 1. Sales API (Data Source Layer)

The pipeline begins with a **Sales API**, which provides raw transactional data.

### 🔍 Data Includes:

* Product details
* Customer information
* Region and location data
* Sales channel information
* Promotions and discounts
* Transaction metrics (quantity, cost, profit)
* Date and time data

### 💡 Purpose:

Acts as the **primary data source**, ensuring continuous and reliable data flow into the system.

---

## ⚙️ 2. Data Ingestion Pipeline (Python Scripts)

This layer automates the process of extracting and loading data.

### 🛠️ Components:

* `api_fetch.py` → Fetches data from API
* Scheduler (Cron / Task Scheduler)
* Logging & error handling

### 🔍 Responsibilities:

* API calls and authentication
* Data extraction and parsing
* Initial validation
* Storing raw data

### 💡 Purpose:

Ensures **automated, consistent, and scalable data ingestion**.

---

## 🧹 3. Data Cleaning & Transformation

Raw data is transformed into a structured and analysis-ready format.

### 🔍 Key Operations:

* Handling missing/null values
* Removing duplicates
* Standardizing formats
* Creating calculated fields (profit, revenue)
* Normalizing data into fact and dimension tables

### 💡 Purpose:

Ensures **high-quality, consistent, and reliable data** for analytics.

---

## 🏗️ 4. Data Warehouse (Star Schema - Model View)

This stage reflects the **Power BI Model View shown in the project**, where all tables are connected in a star schema format.

---

### ⭐ Fact Table

#### `fact_sales`

Stores transactional data and metrics.

**Key Columns:**

* `product_id`
* `region_id`
* `customer_id`
* `channel_id`
* `promotion_id`
* `date_id`
* `quantity`
* `cost`
* `profit`

---

### 📦 Dimension Tables

| Table Name      | Description                    |
| --------------- | ------------------------------ |
| `dim_product`   | Product details                |
| `dim_region`    | Geographic data                |
| `dim_customer`  | Customer segmentation          |
| `dim_channel`   | Sales channel information      |
| `dim_promotion` | Promotion and campaign details |
| `dim_date`      | Date and time attributes       |

---

### 🔗 Relationships (Model View)

All dimension tables are connected to `fact_sales` using **One-to-Many (1 → *) relationships**:

| Fact Column  | Dimension Table |
| ------------ | --------------- |
| product_id   | dim_product     |
| region_id    | dim_region      |
| customer_id  | dim_customer    |
| channel_id   | dim_channel     |
| promotion_id | dim_promotion   |
| date_id      | dim_date        |

---

### 💡 Why This Model?

* ⚡ Fast query performance
* 📊 Efficient aggregations
* 🔍 Easy filtering and slicing
* 📈 Optimized for Power BI dashboards

---

## 🤖 5. AI Summary Table Generation

This layer adds **Generative AI capabilities** to the system.

### 🧠 Process:

1. Extract aggregated data from warehouse tables
2. Apply AI/LLM or rule-based logic
3. Generate human-readable insights
4. Store results in an **AI Summary Table**

---

### 📊 Example Insights:

* 🏆 Top-selling products
* 🌍 Highest revenue regions
* 📦 Category-wise trends
* 📅 Monthly performance summary
* ⚠️ Sales anomalies

---

### 💡 Purpose:

Transforms raw data into **business-friendly insights**, reducing manual analysis effort.

---

## 📊 6. Power BI Dashboard (Model View + Visualization)

The dashboard is built directly on top of the **same star schema model view**.

### 🔍 Features:

* KPI metrics (Revenue, Profit, Orders)
* Time-based analysis using `dim_date`
* Region-wise performance
* Customer segmentation
* Channel performance
* Promotion effectiveness
* AI insights integration

---

### 💡 Purpose:

Provides **interactive and visual analytics** for business users.

---

## 💡 7. Business Insights (Final Output)

This is the final stage where insights are delivered to stakeholders.

### 📈 Key Outcomes:

* Identify top-performing products
* Analyze customer behavior
* Evaluate marketing campaigns
* Optimize sales channels
* Understand regional trends

---

### 💡 Purpose:

Enables **data-driven decision-making** and improves business performance.

---

## 🚀 Architecture Highlights

* 🔄 Fully automated pipeline
* 🧱 Star schema aligned with Power BI Model View
* ⚡ High-performance analytics
* 🤖 AI-powered insights generation
* 📊 Multi-dimensional analysis

---

## 🧠 Summary

This architecture combines:

* ⚙️ Data Engineering (API + ETL)
* 🏗️ Data Warehousing (Star Schema)
* 📊 Business Intelligence (Power BI)
* 🤖 Generative AI (Insights Layer)

👉 Making it a **real-world, production-level analytics system** suitable for modern data roles.

---
