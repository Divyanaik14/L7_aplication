import sqlite3

connection = sqlite3.connect('database/chocolate_house.db')

with connection:
    connection.execute("""
        CREATE TABLE seasonal_flavors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT
        );
    """)
    connection.execute("""
        CREATE TABLE ingredients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            quantity INTEGER
        );
    """)
    connection.execute("""
        CREATE TABLE customer_suggestions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_name TEXT,
            suggestion TEXT,
            allergy_info TEXT
        );
    """)

connection.close()
