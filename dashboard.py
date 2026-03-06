# dashboard.py
import streamlit as st
import pandas as pd
import plotly.express as px
import os

# Page config
st.set_page_config(
    page_title="NYC Taxi Dashboard",
    page_icon="🚕",
    layout="wide"
)

# Load data
SILVER_PATH = r"C:\Users\Lenovo\Downloads\nyc_taxi_project\silver\yellow_trips_silver.parquet"

@st.cache_data
def load_data():
    return pd.read_parquet(SILVER_PATH)

df = load_data()

# Header
st.title("🚕 NYC Taxi Trip Dashboard")
st.markdown("**January 2023 — Yellow Taxi Trip Analysis**")
st.divider()

# ---- Sidebar Filters ----
st.sidebar.header("Filters")

hours = st.sidebar.slider("Pickup Hour", 0, 23, (0, 23))
payment = st.sidebar.multiselect(
    "Payment Type",
    options=df["payment_type_label"].unique(),
    default=df["payment_type_label"].unique()
)

# Apply filters
filtered = df[
    (df["pickup_hour"] >= hours[0]) &
    (df["pickup_hour"] <= hours[1]) &
    (df["payment_type_label"].isin(payment))
]

# ---- KPI Metrics ----
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Trips",    f"{len(filtered):,}")
col2.metric("Total Revenue",  f"${filtered['total_amount'].sum():,.0f}")
col3.metric("Avg Fare",       f"${filtered['fare_amount'].mean():.2f}")
col4.metric("Avg Tip %",      f"{filtered['tip_percentage'].mean():.1f}%")

st.divider()

# ---- Charts ----
col1, col2 = st.columns(2)

with col1:
    hourly = filtered.groupby("pickup_hour").size().reset_index(name="trips")
    fig = px.bar(hourly, x="pickup_hour", y="trips",
                 title="Trips by Hour of Day",
                 color="trips", color_continuous_scale="Blues")
    st.plotly_chart(fig, use_container_width=True)

with col2:
    payment_counts = filtered["payment_type_label"].value_counts().reset_index()
    payment_counts.columns = ["payment_type", "count"]
    fig = px.pie(payment_counts, names="payment_type", values="count",
                 title="Payment Method Breakdown")
    st.plotly_chart(fig, use_container_width=True)

col1, col2 = st.columns(2)

with col1:
    daily = filtered.groupby("pickup_date")["total_amount"].sum().reset_index()
    fig = px.line(daily, x="pickup_date", y="total_amount",
                  title="Daily Revenue", color_discrete_sequence=["green"])
    st.plotly_chart(fig, use_container_width=True)

with col2:
    zones = (filtered.groupby("pickup_location_id").size()
             .reset_index(name="trips")
             .sort_values("trips", ascending=False)
             .head(10))
    fig = px.bar(zones, x="pickup_location_id", y="trips",
                 title="Top 10 Busiest Pickup Zones",
                 color="trips", color_continuous_scale="Reds")
    st.plotly_chart(fig, use_container_width=True)

st.divider()
st.caption("Data Source: NYC Taxi & Limousine Commission | Built with Streamlit")