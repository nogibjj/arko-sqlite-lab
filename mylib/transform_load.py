"""
Transforms and Loads data into the local SQLite3 database
Example:
,general name,count_products,ingred_FPro,avg_FPro_products,avg_distance_root,ingred_normalization_term,semantic_tree_name,semantic_tree_node
"""
import sqlite3
import csv
import os

#load the csv file and insert into a new sqlite3 database
def load(dataset="data/AAPL.csv"):
    """"Transforms and Loads data into the local SQLite3 database"""

    #prints the full working directory and path
    print(os.getcwd())
    with open(dataset, newline='') as csvfile:
        payload = csv.reader(csvfile, delimiter=',')

        # Get the header from the CSV (first row contains column names)
        header = next(payload)

        # Format column names to avoid SQL syntax issues (surround with brackets)
        formatted_header = [f'[{col}]' for col in header]

        # Connect to (or create) the SQLite3 database
        conn = sqlite3.connect('AAPL.db')
        c = conn.cursor()

        # Drop the table if it already exists
        c.execute("DROP TABLE IF EXISTS AAPL")

        # Dynamically create the table based on the CSV header
        columns = ', '.join(formatted_header)
        create_table_query = f"CREATE TABLE AAPL ({columns})"
        c.execute(create_table_query)

        # Prepare the placeholders for the `INSERT INTO` statement
        placeholders = ', '.join(['?' for _ in formatted_header])

        # Insert the data into the table
        insert_query = f"INSERT INTO AAPL ({columns}) VALUES ({placeholders})"
        c.executemany(insert_query, payload)

        # Commit changes and close connection
        conn.commit()
        conn.close()

        print("CSV file has been successfully loaded into AAPL.db")
        return "AAPL.db"

