#group by used to group rows having the same value together.

import numpy as np
import pandas as pd

data = {
    'Category': ['A', 'B', 'A', 'B', 'A', 'B', 'A', 'B'],
    'Store': ['S1', 'S1', 'S2', 'S2', 'S1', 'S2', 'S2', 'S1'],
    'Sales': [100, 200, 150, 250, 120, 180, 200, 300],
    'Quantity': [10, 15, 12, 18, 8, 20, 15, 25],
    'Date': pd.date_range('2023-01-01', periods=8)
}
df = pd.DataFrame(data)
cat=df.groupby('Category')
for i , v in cat:  # i is group name and v is dataframe
    print(i)
    print(v)

#Group by category and calculate the sum of sales
cat = df.groupby('Category')['Sales'].sum()
print(cat)

#group by store ad calculate the sum of sales
cat = df.groupby('Store')['Sales'].sum()
print(cat)

#group by multiple columns
cat = df.groupby(['Category','Store'])['Sales'].sum()
print(cat)