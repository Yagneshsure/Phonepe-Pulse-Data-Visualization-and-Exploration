import os
import csv
import re
import mysql.connector

# database credentials
host = "localhost"
user = "root"
password = "12345"
database = "PhonePe_plus_database"

# Establish a connection to MySQL server without specifying a database
connection = mysql.connector.connect(
    host=host,
    user=user,
    password=password
)

cursor = connection.cursor()

# Create the 'PhonePe2' database if it doesn't exist
cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database}")

# Switch to the 'PhonePe2' database
cursor.execute(f"USE {database}")

# Close the initial connection
connection.close()

# Establish a new connection to the 'PhonePe2' database
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

    # Read the CSV file
    with open(os.path.join(csv_directory, csv_file), 'r') as file:
        csv_reader = csv.reader(file)
        header_row = next(csv_reader)  # Get the header row

        # Create the table with the specified column names
        create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} ("
        create_table_query += ", ".join([f"`{col}` TEXT" for col in header_row])
        create_table_query += ")"
        cursor.execute(create_table_query)

        # Insert data into the table, starting from the second row
        for row in csv_reader:
            insert_query = f"INSERT INTO {table_name} VALUES ({', '.join(['%s'] * len(row))})"
            cursor.execute(insert_query, tuple(row))

# Commit the changes and close the connection
connection.commit()
connection.close()