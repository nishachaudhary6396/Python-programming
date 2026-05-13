import numpy as np
import pandas as pd

#finding Missing Data
data = {
    'A': [1,2,np.nan, 4, 5],
    'B': [np.nan , 2, 3,4,5],
    'C': [1,2,3,np.nan,5],
    'D': [1,np.nan,np.nan,np.nan,5]
}
df = pd.DataFrame(data)
print(df)
print(df.isna().sum()) #will sum the null values
print(df.isna().any()) # will check in each column consist null value
print(df.dropna(thresh=3)) # will drop row which have less than 3 non null values
print(df.fillna(0))   # to fill the null values with 0
values = {'A':0,'B':35,'C':24,'D':50}
print(df.fillna(value=values))
print(df.fillna(df.mean()))  # columnwise
# print(df.dropna())
