#Series gives you indexing,filtering,handling missing values,fast processing. We use Series beacuse python lists only stores values

import pandas as pd
import numpy as np
lebels = ['a','b','c']
my_list = [10,20,30]
arr = np.array([10,20,30])
d = {1:5,2:10,3:15}

print(pd.Series(my_list))   
print(pd.Series(my_list,index = lebels))

print(pd.Series(arr,index = lebels)) 
print(pd.Series(d))