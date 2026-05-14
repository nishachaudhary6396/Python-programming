import numpy as np
import pandas as pd
df =pd.read_csv('pandas/anime.csv')
# print(df.head())  #top 5 rows
# print(df.loc[1]['Title'])  #row at index 1

def extract_episode(txt):
    check = False
    data = ""
    for i in txt:
        if i == ")":
           check = False
           return data
        if check == True:
            data +=i
        if i == "(":
            check = True
    return data

df["Episodes"]=(df["Title"].apply(extract_episode))
print(df)
df['Episodes'] = df['Episodes'].str.replace(" eps","")
df["Episodes"] = df['Episodes'].astype(int)
print(df)