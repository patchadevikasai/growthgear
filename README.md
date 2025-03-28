# Gen AI Analytics - Mini Data Query Simulation Engine

## 🚀 Overview
This project is a **lightweight backend service** that simulates a simplified version of a **Gen AI Analytics** tool. It allows users to query data using natural language and get simulated responses.

## 🎯 Features
- **Natural Language Query Processing** (`/query`)
- **Query Explanation** (`/explain`)
- **Query Validation** (`/validate`)
- **Mock Database Connection**
- **Basic Error Handling & Authentication**

## 🛠️ Tech Stack
- **Language:** Python 🐍
- **Framework:** FastAPI ⚡
- **Database:** SQLite (Mock) 🗃️
- **Deployment:** Render 🌐

## 📂 Project Structure
```
📦 gen-ai-analytics
├── 📄 main.py                # FastAPI app entry point
├── 📄 utils.py               # Helper functions for query processing
├── 📄 auth.py                # API key validation logic
├── 📄 requirements.txt       # Dependencies
├── 📄 .env                   # Environment variables
└── 📄 README.md              # Project documentation
```

## 🏗️ Setup Instructions
### 1️⃣ Clone the Repository
```sh
git clone https://github.com/yourusername/gen-ai-analytics.git
cd gen-ai-analytics
```
### 2️⃣ Create a Virtual Environment & Install Dependencies
```sh
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
pip install -r requirements.txt
```
### 3️⃣ Run the Application
```sh
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```
### 4️⃣ Access the API Docs
Once the app is running, visit:
- **Swagger UI:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **Redoc:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 🔑 API Endpoints
### **1️⃣ Process Query (`/query`)**
#### Request (POST)
```json
{
  "query": "total revenue in Q1 2024"
}
```
#### Response
```json
{
  "query": "total revenue in Q1 2024",
  "sql": "SELECT SUM(revenue) FROM sales WHERE quarter='Q1' AND year=2024",
  "result": {"total_revenue": 500000}
}
```
### **2️⃣ Explain Query (`/explain`)**
#### Request (POST)
```json
{
  "query": "total revenue in Q1 2024"
}
```
#### Response
```json
{
  "query": "total revenue in Q1 2024",
  "breakdown": {
    "metric": "SUM(revenue)",
    "time_period": "Q1 2024",
    "table": "sales"
  }
}
```
### **3️⃣ Validate Query (`/validate`)**
#### Request (POST)
```json
{
  "query": "total revenue in Q1 2024"
}
```
#### Response
```json
{
  "query": "total revenue in Q1 2024",
  "valid": true
}
```

---

## 🔐 Authentication
This API requires an API key for authorization.
- **How to use it in Swagger UI?**
  - Click **Authorize** in [Swagger UI](https://growthgear.onrender.com/docs)
  - Enter your API key and click **Authorize**

- **Using API Key in `curl`?**
```sh
curl -X 'POST' 'https://growthgear.onrender.com/query' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -H 'api_key: YOUR_SECRET_KEY' \
  -d '{ "query": "total revenue in Q1 2024" }'
```

---

## 🌍 Deployment
### **Deployed on Render** ✅
The backend is live at: **[https://growthgear.onrender.com](https://growthgear.onrender.com)**

- API Docs: [https://growthgear.onrender.com/docs](https://growthgear.onrender.com/docs)


---

## 📜 License
This project is open-source and available under the **MIT License**.

---

## 📧 Contact
For queries, reach out at: devikasai50@gmail.com

