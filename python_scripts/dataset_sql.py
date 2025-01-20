import sqlite3
import pandas as pd

conn = sqlite3.connect('../sales_data.db')

df = pd.read_csv('../sales_data.csv')

df.to_sql('Sales', conn, if_exists='replace', index=False)

print("Data imported into SQLite successfully!")