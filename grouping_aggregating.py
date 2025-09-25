# Grouping & Aggregating Data
grouped = df.groupby('Region')['Revenue'].sum()
summary = df.groupby('Product').agg({'Units': 'sum', 'Revenue': 'sum'})
multi_group = df.groupby(['Region', 'Product'])['Revenue'].sum()
summary_reset = df.groupby('Region')['Revenue'].sum().reset_index()
avg_revenue = df.groupby('SalesPerson')['Revenue'].mean()
transactions = df.groupby('Region')['Revenue'].count()
