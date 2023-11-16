import os
import mysql.connector
import csv
import re

# Replace these values with your database credentials
host = "localhost"
user = "root"
password = "12345"
database = "PhonePe"

# Establish a connection to the 'PhonePe' database
connection = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

cursor = connection.cursor()

# Directory where your CSV files are located
csv_directory = 'C:/Users/User/OneDrive/Desktop/Guvi tasks/capston projects/PhonePe_Plue/extracted_data'

# List all CSV files in the directory
csv_files = [f for f in os.listdir(csv_directory) if f.endswith('.csv')]

for csv_file in csv_files:
    # Sanitize the table name by removing invalid characters
    table_name = re.sub(r'[^a-zA-Z0-9_]', '_', os.path.splitext(csv_file)[0])

    # Read the CSV file and insert data into the corresponding table
    with open(os.path.join(csv_directory, csv_file), 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip the header row if it exists

        # Create the table with the same columns as the CSV
        create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} ("
        create_table_query += ", ".join([f"`{col}` TEXT" for col in next(csv_reader)])  # Enclose column names in backticks
        create_table_query += ")"
        cursor.execute(create_table_query)

        # Insert data into the table
        for row in csv_reader:
            insert_query = f"INSERT INTO {table_name} VALUES ({', '.join(['%s'] * len(row))})"
            cursor.execute(insert_query, tuple(row))

# Commit the changes and close the connection
connection.commit()
connection.close()
