# ⚙️ Installation & Requirements

AI-Powered Sales Intelligence Dashboard

---

## 📦 Project Dependencies

This project uses the following Python libraries:

```txt
fastapi==0.111.0
uvicorn==0.30.1
requests==2.32.3
pyodbc==5.1.0
pandas==2.2.2
python-dotenv==1.0.1
```

---

## 🚀 Setup Guide (Step-by-Step)

Follow these steps to run the project locally.

---

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/genai-sales-intelligence-dashboard.git
cd genai-sales-intelligence-dashboard
```

---

### 2️⃣ Create Virtual Environment (Recommended)

```bash
python -m venv venv
```

Activate environment:

**Windows:**

```bash
venv\Scripts\activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Configure Environment Variables

Create a `.env` file in the root folder:

```env
DB_SERVER=localhost
DB_NAME=Sales_GenAI_Analytics
```

---

### 5️⃣ Run the API Server

```bash
uvicorn sales_api:app --reload
```

API will be available at:

```
http://127.0.0.1:8000/docs
```

---

### 6️⃣ Run Data Ingestion Script

```bash
python ingest_sales.py
```

---

### 7️⃣ Generate Executive Intelligence Summary

```bash
python generate_executive_engine.py
```

---

### 8️⃣ Open Power BI Dashboard

* Open `.pbix` file
* Click **Refresh**
* View updated insights

---

## 🧠 Notes

* Ensure SQL Server is running before executing scripts
* Update database connection details if required
* API must be running before ingestion

---

## ⚠️ Troubleshooting

| Issue              | Solution                            |
| ------------------ | ----------------------------------- |
| API not responding | Make sure FastAPI server is running |
| Database error     | Check SQL Server connection         |
| Missing data       | Run ingestion script again          |

---

## ✅ System Requirements

* Python 3.10+
* SQL Server (Local)
* Power BI Desktop
* Windows OS (for Task Scheduler automation)

---

## 📌 Summary

This setup enables:

✔ Real-time data simulation
✔ Automated ingestion
✔ AI-driven executive insights
✔ Interactive Power BI reporting

---

⭐ If this project helps you, consider giving it a star!
