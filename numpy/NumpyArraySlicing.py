#Slicing Arrays
import numpy as np
arr = np.array([1,2,3,4,5,6,7])
print(arr[1:5])     #out will be [2 3 4 5]

#Another Example->
arr1 = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[4:])

#Negative Slicing->
arr2 = np.array([1,2,3,4,5,6,7])
print(arr2[-1:-6:-1])

#Slicing 2-D Arrays->
arr3 = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr3[1,2:4])
