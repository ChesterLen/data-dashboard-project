import pandas as pd

data = {
    'TransactionID': [1, 2, 3],
    'CustomerName': ['John Doe', 'Jane Smith', 'Bob Johnson'],
    'Product': ['Laptop', 'Smartphone', 'Shirt'],
    'Category': ['Electronics', 'Electronics', 'Clothing'],
    'Quantity': [1, 2, 3],
    'Price': [1200.00, 800.00, 30.00],
    'TransactionDate': ['2024-01-01', '2024-01-02', '2024-01-03']
}

df = pd.DataFrame(data)

df.to_csv('sales_data.csv', index=False)

print("Dataset created successfully!")