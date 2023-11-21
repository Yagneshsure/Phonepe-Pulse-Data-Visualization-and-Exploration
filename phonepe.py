# # Required libraries
# import streamlit as st
# import pandas as pd
# import plotly.express as px
# import mysql.connector
# from PIL import Image

# # Connect to MySQL database
# connection = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="12345",
#     database="PhonePe_database"
# )

# # Function to fetch data from MySQL
# def fetch_data(table_name):
#     query = f"SELECT * FROM {table_name}"
#     cursor = connection.cursor()
#     cursor.execute(query)
#     columns = [col[0] for col in cursor.description]
#     data = cursor.fetchall()
#     cursor.close()
#     return pd.DataFrame(data, columns=columns)

# icon = Image.open("images\phonepe_logo.png")
# st.set_page_config(
#     page_title="Phonepe Pulse Data Visualization & Exploration | By YAGNESH SURE",
#     page_icon=icon,
#     layout="wide"
# )

# # Display the image
# st.image(icon, caption="PhonePe Image", use_column_width=True)

# st.title("Welcome to Phonepe Dashboard by YAGNESH SURE")
# st.subheader("Explore and visualize PhonePe data with ease!")


# # Brief description about PhonePe
# st.markdown(
#     """
#     [PhonePe](https://www.phonepe.com/) is a leading digital payment platform in India 
#     that enables users to make payments, recharge, and manage various financial transactions 
#     seamlessly through their mobile devices. With a user-friendly interface and a wide range 
#     of services, PhonePe has become an integral part of the digital payment ecosystem in India.
#     """
# )

# # Select either "Transaction" or "User"
# data_type = st.radio("Select Transaction or User", ["Transaction", "User"])


# # Select relevant table options based on data type
# if data_type.lower() == "transaction":
#     table_options = {
#         "agg_transaction": "Aggregate Transaction",
#         "map_transaction": "Mapped Transaction",
#         "top_transaction": "Top Transaction"
#     }
# else:
#     table_options = {
#         "agg_user": "Aggregate User",
#         "map_user": "Mapped User",
#         "top_user": "Top User"
#     }

# st.subheader(f"Please select the {data_type.lower()} table for visualization:")

# # Dropdown for user to select the table
# selected_table = st.selectbox(f"Select {data_type} Table", list(table_options.keys()), format_func=lambda option: table_options[option])


# # Option to select between "All Regions" and "Specific State"
# region_option = st.radio("Select Region", ["All Region", "Specific State"])

# # List of all states in India
# all_states = [
#     "Andaman and Nicobar Islands", "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar",
#     "Chandigarh", "Chhattisgarh", "Dadra and Nagar Haveli and Daman and Diu", "Delhi", "Goa",
#     "Gujarat", "Haryana", "Himachal Pradesh", "Jharkhand", "Karnataka", "Kerala", "Lakshadweep",
#     "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha",
#     "Puducherry", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh",
#     "Uttarakhand", "West Bengal"
# ]

# # If the user selects "Specific State," provide a dropdown to choose the state
# selected_state = ""
# if region_option == "Specific State":
#     selected_state = st.selectbox("Select State", all_states)
    
# # Option to select the year
# selected_year = st.selectbox("Select Year", list(range(2018, 2024)))

# # Option to select the quarter
# selected_quarter = st.selectbox("Select Quarter", ["Q1", "Q2", "Q3", "Q4"])

    
    
# # Filter table options based on selected data type
# filtered_table_options = {key: value for key, value in table_options.items() if data_type.lower() in key}

# # Fetch top 10 records for the selected table and state
# if selected_state:
#     st.subheader(f"Top 10 records for {filtered_table_options[selected_table]} in {selected_state} - {selected_year} {selected_quarter}")
# else:
#     st.subheader(f"Top 10 records for {filtered_table_options[selected_table]} - {selected_year} {selected_quarter}")

# # Function to fetch top 10 records from MySQL
# def fetch_top_10_records(table_name, selected_state):
#     # Print the selected state for debugging
#     print(f"Selected State: {selected_state}")

#     # Modify the query to filter by state if applicable
#     if selected_state:
#         # Assuming 'State' is the column containing state information
#         query = f"SELECT * FROM {table_name} WHERE State = '{selected_state}' LIMIT 10"
#     else:
#         query = f"SELECT * FROM {table_name} LIMIT 10"

#     cursor = connection.cursor()
#     cursor.execute(query)
#     columns = [col[0] for col in cursor.description]
#     data = cursor.fetchall()
#     cursor.close()
#     return pd.DataFrame(data, columns=columns)


# # Fetch top 10 records and display
# df_top_10 = fetch_top_10_records(selected_table, selected_state)
# st.dataframe(df_top_10)


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

# Select either "Transaction" or "User"
data_type = st.radio("Select Transaction or User", ["Transaction", "User"])

# Select relevant table options based on data type
if data_type.lower() == "transaction":
    table_options = {
        "agg_transaction": "Aggregate Transaction",
        "map_transaction": "Mapped Transaction",
        "top_transaction": "Top Transaction"
    }
else:
    table_options = {
        "agg_user": "Aggregate User",
        "map_user": "Mapped User",
        "top_user": "Top User"
    }

# Filter table options based on selected data type
filtered_table_options = {key: value for key, value in table_options.items() if data_type.lower() in key}

st.subheader(f"Please select the {data_type.lower()} table for visualization:")

# Dropdown for user to select the table
selected_table = st.selectbox(f"Select {data_type} Table", list(table_options.keys()), format_func=lambda option: table_options[option])

# Fetch data from the selected table
df_data = fetch_data(selected_table)

# Get the user-friendly display name for the selected table
display_name = table_options.get(selected_table, selected_table)

# Add debugging information to check if data is fetched
st.write(f"Data from {display_name} table:")
st.dataframe(df_data)

# Option to select between "All Regions" and "Specific State"
region_option = st.radio("Select Region Option", ["All Region", "Specific State"])

# Mapping of states
state_options = {
    "andaman-&-nicobar-islands": "Andaman and Nicobar Islands",
    "andhra-pradesh": "Andhra Pradesh",
    "arunachal-pradesh": "Arunachal Pradesh",
    "assam": "Assam",
    "bihar": "Bihar",
    "chandigarh": "Chandigarh",
    "chhattisgarh": "Chhattisgarh",
    "dadra-&-nagar-haveli-&-daman-&-diu": "Dadra and Nagar Haveli and Daman and Diu",
    "delhi": "Delhi",
    "goa": "Goa",
    "gujarat": "Gujarat",
    "haryana": "Haryana",
    "himachal-pradesh": "Himachal Pradesh",
    "jammu-&-kashmir": "Jammu and Kashmir",
    "jharkhand": "Jharkhand",
    "karnataka": "Karnataka",
    "kerala": "Kerala",
    "lakshadweep": "Lakshadweep",
    "madhya-pradesh": "Madhya Pradesh",
    "maharashtra": "Maharashtra",
    "manipur": "Manipur",
    "meghalaya": "Meghalaya",
    "mizoram": "Mizoram",
    "nagaland": "Nagaland",
    "odisha": "Odisha",
    "puducherry": "Puducherry",
    "punjab": "Punjab",
    "rajasthan": "Rajasthan",
    "sikkim": "Sikkim",
    "tamil-nadu": "Tamil Nadu",
    "telangana": "Telangana",
    "tripura": "Tripura",
    "uttar-pradesh": "Uttar Pradesh",
    "uttarakhand": "Uttarakhand",
    "west-bengal": "West Bengal",
    "ladakh": "Ladakh",
    "arunachal-pradesh": "Arunachal Pradesh",
    "assam": "Assam",
    "bihar": "Bihar",
    "chandigarh": "Chandigarh",
    "chhattisgarh": "Chhattisgarh",
    "dadra-&-nagar-haveli-&-daman-&-diu": "Dadra and Nagar Haveli and Daman and Diu",
    "goa": "Goa",
    "gujarat": "Gujarat",
    "haryana": "Haryana",
    "himachal-pradesh": "Himachal Pradesh",
    "jammu-&-kashmir": "Jammu and Kashmir",
    "jharkhand": "Jharkhand",
    "karnataka": "Karnataka",
    "kerala": "Kerala",
    "lakshadweep": "Lakshadweep",
}

# If the user selects "Specific State," provide a dropdown to choose the state
selected_state = ""
if region_option == "Specific State":
    selected_state = st.selectbox("Select State", list(state_options.keys()), format_func=lambda option: state_options[option])

# Option to select the year
selected_year = st.selectbox("Select Year", list(range(2018, 2024)))

# Option to select the quarter
selected_quarter = st.selectbox("Select Quarter", ["Q1", "Q2", "Q3", "Q4"])

# Filter table options based on selected data type
filtered_table_options = {key: value for key, value in table_options.items() if data_type.lower() in key}

# Fetch top 10 records for the selected table and state
if selected_state:
    st.subheader(f"Top 10 records for {filtered_table_options[selected_table]} in {state_options[selected_state]} - {selected_year} {selected_quarter}")
else:
    st.subheader(f"Top 10 records for {filtered_table_options[selected_table]} - {selected_year} {selected_quarter}")

# Function to fetch top 10 records from MySQL
def fetch_top_10_records(table_name, selected_state):
    # Print the selected state for debugging
    print(f"Selected State: {selected_state}")

    # Modify the query to filter by state if applicable
    if selected_state:
        # Assuming 'State' is the column containing state information
        query = f"SELECT * FROM {table_name} WHERE State = '{selected_state}' LIMIT 10"
    else:
        query = f"SELECT * FROM {table_name} LIMIT 10"

    cursor = connection.cursor()
    cursor.execute(query)
    columns = [col[0] for col in cursor.description]
    data = cursor.fetchall()
    cursor.close()
    return pd.DataFrame(data, columns=columns)

# Fetch top 10 records and display
df_top_10 = fetch_top_10_records(selected_table, selected_state)
st.dataframe(df_top_10)
