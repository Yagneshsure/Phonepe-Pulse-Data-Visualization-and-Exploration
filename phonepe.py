import streamlit as st
import pandas as pd
import plotly.express as px
import mysql.connector

# Connect to MySQL database
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="PhonePe_database"
)

# Function to fetch data from MySQL
def fetch_data(table_name):
    query = f"SELECT * FROM {table_name}"
    cursor = connection.cursor()
    cursor.execute(query)
    columns = [col[0] for col in cursor.description]
    data = cursor.fetchall()
    cursor.close()
    return pd.DataFrame(data, columns=columns)

# Streamlit App
st.title("PhonePe Pulse Dashboard")

# Dropdown for user to select the table
selected_table = st.selectbox("Select Table", ["agg_transaction", "agg_user", "map_transaction", "map_user", "top_transaction", "top_user"])

# Fetch data based on user selection
data = fetch_data(selected_table)

# Display raw data
st.subheader("Raw Data")
st.write(data)

# Dropdown for user to select a metric
selected_metric = st.selectbox("Select Metric", data.columns)

# Plotly Express bar chart based on user selection
fig = px.bar(data, x=data.index, y=selected_metric, title=f"{selected_metric} Distribution")
st.plotly_chart(fig)