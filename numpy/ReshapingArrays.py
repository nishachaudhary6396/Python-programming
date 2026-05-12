import numpy as np
arr = np.array([1,2,3,4,5])
print(arr.reshape(5,1))

#Flattening Arrays
arr = np.array([[1,2],[3,4]])
print(arr.flatten()) # convert multidimensional array into 1d array

#Splitting Array
arr1 = np.array([1,2,3,4,5,6])
print(np.split(arr1,3))

#joinning arrays
a = np.array([1,2,3])
b = np.array([4,5,6])
print(np.concatenate((a,b)))