import sqlite3
import pandas as pd

# Step 1: Connect to SQLite database (Creates 'snapdeal.db' if it doesn't exist)
conn = sqlite3.connect("snapdeal.db")
cursor = conn.cursor()

# Step 2: Create a table (Modify column names based on CSV structure)
cursor.execute("""
CREATE TABLE IF NOT EXISTS snapdeal_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Product_name TEXT,
    Price REAL,
    Rating REAL
)
""")
conn.commit()

# Step 3: Load the CSV file
csv_file = "/mnt/data/cleaned_snapdeal_data.csv"  # Path where your file is stored
df = pd.read_csv(csv_file)

# Step 4: Insert data into the table
df.to_sql("snapdeal_data", conn, if_exists="replace", index=False)

# Step 5: Query data to check if insertion was successful
query = "SELECT * FROM snapdeal_data LIMIT 5"
result = pd.read_sql_query(query, conn)
print(result)

# Step 6: Close the database connection
conn.close()
