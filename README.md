# 🚀 AI-Powered Sales Intelligence Dashboard

## 📌 Overview

The **AI-Powered Sales Intelligence Dashboard** is a full-stack, end-to-end data analytics project that simulates real-time sales data, processes it through an automated pipeline, and generates executive-level business insights.

This system integrates **data engineering, analytics, and AI-driven decision intelligence** to help business stakeholders understand performance, identify risks, and take strategic actions.

---

## 🎯 Key Objectives

* Build a **real-time data ingestion pipeline**
* Design a **scalable star schema data warehouse**
* Develop an **interactive Power BI dashboard**
* Generate **automated executive summaries**
* Enable **decision-making using AI-inspired intelligence**

---

## 🏗️ System Architecture

```
Sales API (FastAPI)
        ↓
Data Ingestion Script (Python)
        ↓
SQL Server (Star Schema Warehouse)
        ↓
Executive Intelligence Engine (Python)
        ↓
Power BI Dashboard (Visualization Layer)
```

---

## ⚙️ Features

### 🔄 Automated Data Pipeline

* Simulates real-time sales using a custom API
* Ingests data into SQL Server every few minutes
* Handles structured storage using a star schema

### 🧠 Executive Intelligence Engine

* Generates business summaries without LLM dependency
* Detects:

  * Growth trends
  * Profitability risks
  * Top-performing regions & categories
* Provides **actionable recommendations**

### 📊 Power BI Dashboard

* Multi-page interactive report
* Includes:

  * Sales Overview
  * Time Intelligence
  * Geographic Insights (India-focused)
  * Product & Customer Analysis
  * Risk & Performance Monitoring
* Executive dashboard with **AI-generated summary**

### ⚠️ Risk Scoring System

* Automatically classifies business health:

  * 🟢 Stable
  * 🟡 Moderate Risk
  * 🔴 High Risk

---

## 🗄️ Data Model (Star Schema)

### Fact Table

* `fact_sales` → Stores transactional data

### Dimension Tables

* `dim_product` → Product details (category, brand, price range)
* `dim_region` → Indian geography (state, city, region)
* `dim_customer` → Customer segmentation
* `dim_channel` → Sales channels (online/offline)
* `dim_promotion` → Campaigns & discounts
* `dim_date` → Time intelligence

---

## 🛠️ Tech Stack

| Layer           | Technology             |
| --------------- | ---------------------- |
| Data Generation | FastAPI                |
| Data Processing | Python                 |
| Database        | SQL Server             |
| Visualization   | Power BI               |
| Automation      | Windows Task Scheduler |
| Version Control | Git & GitHub           |

---

## 🔄 Automation Workflow

* ⏱ Sales data generated every 5 minutes
* ⚙️ Data ingestion runs automatically
* 🧠 Executive summary generated periodically
* 📊 Power BI refreshes with updated insights

---

## 🚀 How to Run the Project

### 1️⃣ Start API

```bash
uvicorn sales_api:app --reload
```

### 2️⃣ Run Data Ingestion

```bash
python ingest_sales.py
```

### 3️⃣ Generate Executive Summary

```bash
python generate_executive_engine.py
```

### 4️⃣ Open Power BI Dashboard

* Load `.pbix` file
* Click **Refresh**

---

## 📸 Dashboard Highlights

* KPI Cards (Revenue, Profit, Orders)
* Region-wise performance (India map)
* Product profitability analysis
* Channel performance insights
* AI-generated executive summary

---

## 💡 Key Learnings

* End-to-end data pipeline design
* Star schema modeling for analytics
* Business intelligence dashboarding
* Automation using task scheduling
* AI-inspired decision intelligence systems

---

## 📈 Future Enhancements

* Integrate real LLM APIs (OpenAI / Gemini)
* Deploy pipeline on cloud (Azure / AWS)
* Add anomaly detection & forecasting
* Enable real-time streaming dashboards
* Email alerts for business risks

---

## 👨‍💻 Author

**Tejas Kapse**
