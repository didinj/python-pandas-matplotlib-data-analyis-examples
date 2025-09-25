# Inspecting & Selecting Data
print(df.columns.tolist())
print(df.head())

# Selecting columns
sales_person = df['SalesPerson']
subset = df[['Date', 'Region', 'Product', 'Units']]

# Filtering rows
north_sales = df[df['Region'] == 'North']
south_high_units = df[(df['Region'] == 'South') & (df['Units'] > 5)]

# Using .loc and .iloc
print(df.loc[0:3, ['Date', 'Units']])
print(df.iloc[0:5, 0:3])
