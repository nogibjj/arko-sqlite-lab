"""Query the database"""

import sqlite3


def query():
    """Query the database for the top 5 rows of the GroceryDB table"""
    conn = sqlite3.connect("AAPL.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM AAPL")
    print("Top 5 rows of the AAPL table:")
    print(cursor.fetchall())
    conn.close()
    return "Success"


