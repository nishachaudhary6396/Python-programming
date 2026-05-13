import numpy as np
import pandas as pd

df1 = pd.DataFrame({
    'name': ['Nisha','Khushi','Shaurya','Anushka']
}, index=[1,2,3,4])

df2 = pd.DataFrame({
    'score': [85,65,78]
}, index=[2,3,4])

print(df1)
print(df2)
print(df1.join(df2))