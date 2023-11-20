# Required libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import mysql.connector
from PIL import Image

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

icon = Image.open("images\phonepe_logo.png")
st.set_page_config(
    page_title="Phonepe Pulse Data Visualization & Exploration | By YAGNESH SURE",
    page_icon=icon,
    layout="wide"
)

# Display the image
st.image(icon, caption="PhonePe Image", use_column_width=True)

st.title("Welcome to Phonepe Dashboard by YAGNESH SURE")
st.subheader("Explore and visualize PhonePe data with ease!")


# Brief description about PhonePe
st.markdown(
    """
    [PhonePe](https://www.phonepe.com/) is a leading digital payment platform in India 
    that enables users to make payments, recharge, and manage various financial transactions 
    seamlessly through their mobile devices. With a user-friendly interface and a wide range 
    of services, PhonePe has become an integral part of the digital payment ecosystem in India.
    """
)


st.subheader("Please select the table for visualization:")

# Dropdown for user to select the table with renamed options
table_options = {
    "agg_transaction": "Aggregate Transaction",
    "agg_user": "Aggregate User",
    "map_transaction": "Mapped Transaction",
    "map_user": "Mapped User",
    "top_transaction": "Top Transaction",
    "top_user": "Top User"
}


# Dropdown for user to select the table
selected_table = st.selectbox("Select Table", list(table_options.keys()), format_func=lambda option: table_options[option])