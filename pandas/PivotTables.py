#pivot table...if you want to use your columns , your index , your values than you use pivot tables
import numpy as np
import pandas as pd
data = {
    'Date': pd.date_range('2023-01-01', periods=20),
    'Product': ['A', 'B', 'C', 'D'] * 5,
    'Region': ['East', 'West', 'North', 'South', 'East', 'West', 'North', 'South', 'East', 'West',
               'North', 'South', 'East', 'West', 'North', 'South', 'East', 'West', 'North', 'South'],
    'Sales': np.random.randint(100, 1000, 20),
    'Units': np.random.randint(10, 100, 20),
    'Rep': ['John', 'Mary', 'Bob', 'Alice', 'John', 'Mary', 'Bob', 'Alice', 'John', 'Mary',
            'Bob', 'Alice', 'John', 'Mary', 'Bob', 'Alice', 'John', 'Mary', 'Bob', 'Alice']
}

df = pd.DataFrame(data)
print(pd.pivot_table(df,values = "Sales",index="Region",columns ="Product"))
print(pd.pivot_table(df,values = "Sales",index="Region",columns ="Product",aggfunc = 'median'))  # using aggregation function

pivot2 = pd.pivot_table(df, values=['Sales','Units'], index='Region',columns='Product')
print(pivot2)

#Cross Tabs  -> how many times each combination occurs
print(pd.crosstab(df['Region'],df['Product']))
