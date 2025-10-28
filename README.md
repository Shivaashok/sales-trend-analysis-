# sales-trend-analysis-

Project Overview:
This project analyzes monthly sales trends from an online sales dataset. The goal is to calculate monthly revenue and order volume to identify trends over time.

Tools Used:

Database: SQLite (can also work with PostgreSQL or MySQL)

Python: For dataset creation and running SQL queries

Pandas: For displaying query results

Dataset:

Table Name: orders

Columns:

order_id: Unique identifier for each order

order_date: Date when the order was placed

amount: Total amount of the order

product_id: Identifier for the product sold

Tasks Performed:

Created an orders table in SQLite.

Generated sample data for one year with random orders per month.

Wrote SQL query to calculate monthly revenue and order volume:

Grouped by year and month

Used SUM() to calculate total revenue

Used COUNT(DISTINCT order_id) to calculate order volume

Ordered results by year and month

How to Run:

Install Python and SQLite if not already installed.

Copy the provided Python script into a .py file.

Run the script using Python.

The script will create the dataset, run the SQL query, and display the results.

Expected Outcome:

A table showing monthly revenue and order volume for each month in the dataset.

Insights into trends such as peak months and revenue patterns.

Notes:

The data is randomly generated for demonstration purposes.

You can modify the script to work with your real dataset.
