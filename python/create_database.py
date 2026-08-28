import pandas as pd
import sqlite3

df = pd.read_csv("../data/processed/sales_90_days_clean.csv")
conn = sqlite3.connect("../data/processed/sales_90_days_clean.db")

df.to_sql("sales", conn, if_exists="replace", index=False)

conn.close()

print("Success.")

conn = sqlite3.connect("../data/processed/sales_90_days_clean.db")

tables = pd.read_sql_query(
    "SELECT name FROM sqlite_master WHERE type='table';",
    conn
)

print(tables)

conn.close()

conn = sqlite3.connect("../data/processed/sales_90_days_clean.db")

test = pd.read_sql_query(
    "SELECT * FROM sales LIMIT 5;",
    conn
)

print(test)

conn.close()