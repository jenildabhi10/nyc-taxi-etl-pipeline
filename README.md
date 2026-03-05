# 🚕 NYC Taxi ETL Pipeline

An end-to-end ETL data pipeline built with Python and Pandas
using the NYC Yellow Taxi Trip dataset (January 2023).

## 🏗️ Architecture
Raw Parquet → Bronze → Silver → Gold

- **Bronze** : Raw data ingested as-is
- **Silver** : Cleaned, filtered and enriched data
- **Gold**   : Business aggregations and insights

## 📊 Dataset
- Source: NYC Taxi & Limousine Commission (TLC)
- Size: ~3 million rows, January 2023
- Format: Parquet

## 🔍 Gold Layer Insights
- Hourly trip stats (peak hours analysis)
- Daily revenue summary
- Payment method breakdown
- Top 10 busiest pickup zones

## 🛠️ Tech Stack
- Python
- Pandas
- PyArrow
- Jupyter Notebook

## ▶️ How to Run
1. Download the dataset from NYC TLC website
2. Install dependencies: `pip install pandas pyarrow`
3. Run notebooks in order:
   - `notebook_1_bronze.ipynb`
   - `notebook_2_silver.ipynb`
   - `notebook_3_gold.ipynb`
