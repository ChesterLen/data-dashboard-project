🛍️ Sales Data Dashboard

    This repository contains all the code and resources for analyzing sales data and creating an interactive dashboard to
    visualize key business metrics using Python and SQL.

📋 Project Overview

    This project demonstrates the following skills:
    
    Querying and analyzing sales data using SQL.
    
    Building an interactive dashboard using Python with Dash and Plotly.
    
    Visualizing key business metrics, such as:
    
    Monthly revenue trends.
    
    Top-selling products.
    
    Customer segmentation by revenue.
    
    Handling real-world challenges like data cleaning and querying.

🚀 Features

    Interactive Dashboard: A dynamic interface to explore sales data interactively.
    
    Visual Insights:
    
    Monthly revenue trends.
    
    Top 5 best-selling products.
    
    Customer spending insights.
    
    Customizable Filters: Filter data by date, product category, or customer.

🔧 Getting Started

    1. Clone the Repository
    
    git clone https://github.com/your-username/sales-data-dashboard.git
    cd sales-data-dashboard
    
    2. Set Up the Environment
    
    Create and activate a virtual environment:
    
    python -m venv env
    source env/bin/activate # For macOS/Linux
    env\Scripts\activate # For Windows
    
    Install the required dependencies:
    
    pip install -r requirements.txt
    
    3. Create or Load the Dataset
    
    Use the create_dataset.py script to generate the dataset:
    
    python src/create_dataset.py
    
    The dataset will be saved as data/sales_data.csv.
    
    4. Import the Dataset into SQL
    
    Run the import_to_sql.py script to import the dataset into a local SQLite database:
    
    python src/import_to_sql.py
    
    5. Run the Dashboard
    
    Start the dashboard application:
    
    python src/dashboard_app.py
    
    Open your browser and navigate to http://127.0.0.1:8050/ to view the dashboard.

📈 Key SQL Queries

    Here are some of the key SQL queries used in this project:
    
    Monthly Revenue:
    
    SELECT strftime('%Y-%m', TransactionDate) AS Month, SUM(Price * Quantity) AS Revenue
    FROM Sales
    GROUP BY Month
    ORDER BY Month;
    
    Top-Selling Products:
    
    SELECT Product, SUM(Quantity) AS TotalQuantity
    FROM Sales
    GROUP BY Product
    ORDER BY TotalQuantity DESC
    LIMIT 5;
    
    Customer Segmentation by Revenue:
    
    SELECT CustomerName, SUM(Price * Quantity) AS TotalSpent
    FROM Sales
    GROUP BY CustomerName
    ORDER BY TotalSpent DESC;

📊 Technologies Used

    Python: Dash, Plotly, Pandas
    
    SQL: SQLite (easily adaptable to MySQL or other databases)
    
    Development Tools: SQLiteStudio, DBeaver