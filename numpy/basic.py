import numpy as np
print(np.__version__)

arr = np.array([1,2,3,4,5])
print(arr)

print(type(arr))

# Dimensions in Arrays
arr = np.array(42)
print(arr)

#2D array
arr2 = np.array([[1,2,3],[4,5,6]])
print(arr2)


# check dimensions of the array by ndim...it tells you the how many dimensions we have
a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

# higher dimnsional Arrays
arr = np.array([1,2,3,4], ndmin = 5)
print(arr)
print('number of dimensions : ', arr.ndim)

#Access 2-D Array
arr3 = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print('3rd element of 2nd row',arr3[1,2])

