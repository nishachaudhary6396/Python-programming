# Combining multiple series
import numpy as np
import pandas as pd

data = {
    'Name' : ['Nisha','Khushi','Mehak','Deepti'],
    'Age' : [20,21,22,21],
    'city' : ['Delhi','Agra','Mumbai','Banglore'],
    'Salary': [50000,60000,55000,65000]
}
data_frame=pd.DataFrame(data)
print(data_frame)

data_list = [
    ['Lira',20,'Delhi',50000],
    ['Peter',21,'Agra',60000],
    ['Sachi',22,'Mumbai',55000],
    ['Anushka',21,'Banglore',65000]
]
columns = ['Name','Age','City','Salary']
df2 = pd.DataFrame(data_list,columns = columns)
print(df2)
print(df2['Name']) # how to selct a single column
print(df2[['Name','City']])  #How to select multiple columns

#Creating a new column
df2['Designation'] = ['Software Developer','Data Scientist','Doctor','IAS']
print(df2)

#Remove a new Column
df2.drop('Designation', axis=1, inplace=True)
print(df2)

#Remove a row
df2.drop(0, axis = 0)

#Selecting a row
print(df2.loc[0]) # loc is location ..used for selecting the row
print(df2.loc[[0,1]])
print(df2.iloc[0])

#Selecting Subsets of Rows and Columns
print(data_frame.loc[[0,1], ["city","Salary"]])
print(df2.loc[[2,3], ['City','Salary']])

#Conditional Selection
print(df2[(df2['Age'] > 21) & (df2['City'] == 'Mumbai')])