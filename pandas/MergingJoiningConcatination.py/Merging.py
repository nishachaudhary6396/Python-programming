import numpy as np
import pandas as pd

employess = pd.DataFrame({
    'employee_id': [1,2,3,4,5],
    'name':['Nisha','Khushi','Shaurya','Anushka','Vishwas'],
    'department':['IT','HR','Finace','HR','IT']
})
salaries = pd.DataFrame({
    'employee_id': [1,2,3,4,5],
    'salary': [50000,60000,70000,80000,90000],
    'bonus': [5000,6000,7000,8000,9000]
})
print(employess)
print(salaries)
print(pd.merge(employess,salaries, on='employee_id',how='inner'))
print(pd.merge(employess,salaries, on='employee_id',how='outer'))
print(pd.merge(employess,salaries, on='employee_id',how='left'))
print(pd.merge(employess,salaries, on='employee_id',how='right'))