from dash import Dash, dcc, html
import plotly.express as px
import pandas as pd
import sqlite3

db_connection = sqlite3.connect('../sales_data.db')
df = pd.read_sql_query('SELECT * FROM Sales', db_connection)

app = Dash(__name__)

monthly_revenue = df.groupby(df['TransactionDate'].str[:7]).apply(
    lambda x: (x['Price'] * x['Quantity']).sum()
).reset_index(name='Revenue')

monthly_revenue_chart = px.bar(monthly_revenue, x='TransactionDate', y='Revenue', title='Monthly Revenue')

app.layout = html.Div([
    html.H1('Sales Dashboard'),
    dcc.Graph(figure=monthly_revenue_chart)
])

if __name__ == '__main__':
    app.run_server(debug=True)