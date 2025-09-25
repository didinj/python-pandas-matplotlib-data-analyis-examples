# Derived Columns & Vectorized Operations
df['Revenue'] = df['Units'] * df['Price']
df['ProfitMargin'] = (df['Revenue'] * 0.2) / df['Revenue'] * 100
df['ProductUpper'] = df['Product'].str.upper()
df['HighValue'] = df['Revenue'] > 100
