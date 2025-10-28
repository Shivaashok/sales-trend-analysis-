import sqlite3
import pandas as pd
import random
from datetime import datetime

# Create in-memory SQLite database
conn = sqlite3.connect(":memory:")
cursor = conn.cursor()

# Create orders table
cursor.execute('''
CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY,
    order_date DATE,
    amount REAL,
    product_id INTEGER
)
''')

# Insert sample data (simulate one year of monthly orders)
data = []
order_id = 1
for month in range(1, 13):
    num_orders = random.randint(50, 100)  # number of orders per month
    for _ in range(num_orders):
        day = random.randint(1,28)  # safe day for all months
        order_date = datetime(2024, month, day)
        amount = round(random.uniform(20, 500), 2)
        product_id = random.randint(1, 20)
        data.append((order_id, order_date.strftime("%Y-%m-%d"), amount, product_id))
        order_id += 1

# Insert into the table
cursor.executemany('INSERT INTO orders VALUES (?,?,?,?)', data)
conn.commit()

# Run the SQL task: Monthly revenue and order volume
query = '''
SELECT
    STRFTIME('%Y', order_date) AS order_year,
    STRFTIME('%m', order_date) AS order_month,
    SUM(amount) AS total_revenue,
    COUNT(DISTINCT order_id) AS order_volume
FROM orders
GROUP BY order_year, order_month
ORDER BY order_year, order_month;
'''

df_result = pd.read_sql_query(query, conn)
print(df_result)
