import numpy as np
import pandas as pd

data = {
    'A': [1, 2, 3, 4, 5],
    'B': [10, 20, 30, 40, 50],
    'C': [100, 200, 300, 400, 500]
}
df = pd.DataFrame(data)
print(df.shape)
print(df.columns)
print(df.info())
print(df.describe())
print(df['A'] + 10)