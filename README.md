# 🚕 NYC Taxi ETL & Analytics Pipeline

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=flat-square&logo=python)
![Pandas](https://img.shields.io/badge/Pandas-2.0+-green?style=flat-square&logo=pandas)
![Plotly](https://img.shields.io/badge/Plotly-Dash-orange?style=flat-square&logo=plotly)
![DuckDB](https://img.shields.io/badge/DuckDB-SQL-yellow?style=flat-square)
![Scikit-learn](https://img.shields.io/badge/ScikitLearn-ML-red?style=flat-square&logo=scikit-learn)
![License](https://img.shields.io/badge/License-MIT-lightgrey?style=flat-square)

An end-to-end **ETL Data Pipeline + Analytics Dashboard** project built with Python,
using the official NYC Yellow Taxi Trip dataset (January 2023, ~3 million rows).

---

## 📌 Project Overview

This project demonstrates a complete data engineering and analytics workflow:

- **Extract** raw Parquet data from NYC TLC open data
- **Transform** it through a 3-layer Medallion Architecture (Bronze → Silver → Gold)
- **Analyze** with SQL using DuckDB
- **Visualize** patterns with Matplotlib & Seaborn
- **Predict** fare amounts using Machine Learning (Linear Regression + Random Forest)
- **Present** everything in an interactive Dash dashboard

---

## 🏗️ Architecture

```
Raw Parquet File (NYC TLC Open Data)
          │
          ▼
    🥉 BRONZE LAYER
    Raw data ingested as-is into Parquet
    No transformations — exact copy of source
          │
          ▼
    🥈 SILVER LAYER
    Cleaned & enriched data
    • Removed nulls and invalid records
    • Fixed data types
    • Added derived columns:
      trip_duration_minutes, avg_speed_mph,
      tip_percentage, pickup_hour, payment_type_label
          │
          ▼
    🥇 GOLD LAYER
    Business-ready aggregations
    • Hourly trip stats
    • Daily revenue summary
    • Payment method breakdown
    • Top 10 busiest pickup zones
          │
          ▼
    📊 ANALYTICS & DASHBOARD
    SQL Analysis → Visualizations → ML → Dashboard
```

---

## 📁 Folder Structure

```
nyc_taxi_project/
│
├── 📓 Notebooks (run in order)
│   ├── 01_bronze_layer.ipynb         # Raw data ingestion
│   ├── 02_silver_layer.ipynb         # Data cleaning & enrichment
│   ├── 03_gold_layer.ipynb           # Business aggregations
│   ├── 04_sql_analysis.ipynb         # SQL queries with DuckDB
│   ├── 05_visualizations.ipynb       # Charts with Matplotlib & Seaborn
│   └── 06_machine_learning.ipynb     # Fare prediction with Scikit-learn
│
├── 📊 Dashboard
│   └── dashboard.py                  # Interactive Dash dashboard
│
├── 📄 Data (not tracked in Git)
│   ├── raw/                          # Original downloaded parquet file
│   ├── bronze/                       # Raw delta/parquet copy
│   ├── silver/                       # Cleaned & enriched parquet
│   └── gold/                         # Aggregated CSVs & chart images
│       ├── hourly_stats.csv
│       ├── daily_revenue.csv
│       ├── payment_breakdown.csv
│       ├── top_zones.csv
│       ├── chart_trips_by_hour.png
│       ├── chart_daily_revenue.png
│       ├── chart_payment_breakdown.png
│       ├── chart_fare_distribution.png
│       └── chart_heatmap.png
│
├── 📋 requirements.txt               # All Python dependencies
├── 🚫 .gitignore                     # Excludes large data files
└── 📖 README.md                      # This file
```

---

## 📊 Dataset

| Property    | Details                                      |
|-------------|----------------------------------------------|
| Source      | NYC Taxi & Limousine Commission (TLC)        |
| Dataset     | Yellow Taxi Trip Records — January 2023      |
| Rows        | ~3,066,766 trips                             |
| Format      | Parquet                                      |
| Size        | ~50 MB                                       |
| Download    | https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2023-01.parquet |

---

## 🔍 Key Insights from Gold Layer

- 🕕 **Peak hours** are 6 PM–8 PM on weekdays
- 💳 **70%+** of trips are paid by credit card
- 💰 **Midtown Manhattan** zones generate the highest revenue
- ⭐ **Late night trips** (1 AM–3 AM) have the highest tip percentages
- 📏 **Average trip distance** is ~3 miles, average fare ~$15

---

## 🤖 Machine Learning Results

Predicting fare amount using trip features:

| Model              | MAE (Avg Error) | R² Score |
|--------------------|-----------------|----------|
| Linear Regression  | ~$2.80          | ~0.85    |
| Random Forest      | ~$1.90          | ~0.93    |

**Most important features:** trip distance, trip duration, pickup location

---

## 🛠️ Tech Stack

| Category         | Tools                              |
|------------------|------------------------------------|
| Language         | Python 3.8+                        |
| Data Processing  | Pandas, PyArrow                    |
| SQL Analysis     | DuckDB                             |
| Visualization    | Matplotlib, Seaborn, Plotly        |
| Machine Learning | Scikit-learn                       |
| Dashboard        | Dash by Plotly, Dash Bootstrap     |
| Storage Format   | Parquet, CSV                       |
| Environment      | Jupyter Notebook / Google Colab    |

---

## ▶️ How to Run

### 1. Clone the repository
```bash
git clone https://github.com/jenildabhi10/nyc-taxi-etl-pipeline.git
cd nyc-taxi-etl-pipeline
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Download the dataset
```bash
# Download from NYC TLC:
# https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2023-01.parquet
# Save it to: raw/yellow_tripdata_2023-01.parquet
```

### 4. Run notebooks in order
```
01_bronze_layer.ipynb  →  02_silver_layer.ipynb  →  03_gold_layer.ipynb
04_sql_analysis.ipynb  →  05_visualizations.ipynb →  06_machine_learning.ipynb
```

### 5. Launch the dashboard
```bash
python dashboard.py
# Open: http://127.0.0.1:8050
```

---

## 📸 Dashboard Features

- 🔢 **KPI Cards** — Total trips, revenue, avg fare, avg tip %
- 📈 **Revenue Trend** — Daily revenue with 7-day ML forecast
- 📊 **Hourly Analysis** — Trip volume by hour with peak highlighting
- 🗺️ **Pickup Heatmap** — Busiest days and hours matrix
- 🥧 **Payment Breakdown** — Credit card vs cash donut chart
- 📍 **Zone Analysis** — Top pickup zones by revenue
- 🔵 **Fare vs Distance** — Scatter plot colored by tip percentage

---

## 🚀 Future Improvements

- [ ] Add multi-month data comparison (2023 full year)
- [ ] Deploy dashboard to Render or Railway (free hosting)
- [ ] Add weather data to analyze impact on trips
- [ ] Build a real-time pipeline with Kafka + Spark Streaming
- [ ] Add geospatial analysis with actual NYC zone shapefiles

---

## 👤 Author

**Jenil Dabhi**
- GitHub: [@jenildabhi10](https://github.com/jenildabhi10)

---

## 📄 License

This project is licensed under the MIT License.

---

*Data provided by NYC Taxi & Limousine Commission (TLC) — publicly available open data.*
