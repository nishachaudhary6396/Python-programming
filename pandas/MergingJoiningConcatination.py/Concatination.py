#Concatination of two dataframe
import pandas as pd
import numpy as np

df1 = pd.DataFrame({
    'A': ['A0','A1','A2','A3'],
    'B': ['B0','B1','B2','B3'],
    'C': ['C0','C1','C2','C3']
})
df2 = pd.DataFrame({
    'A': ['A4','A5','A6','A7'],
    'B': ['B4','B5','B6','B7'],
    'C': ['C4','C5','C6','C7']
})
print(df1)
print(df2)
print(pd.concat([df1,df2]))
print(pd.concat([df1,df2],axis=1))