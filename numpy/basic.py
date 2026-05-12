import numpy as np
print(np.__version__)

arr = np.array([1,2,3,4,5])
print("1 D array")
print(arr.size)
print(arr.dtype)  #print datatype of the array
arr = arr.astype('float')
print(arr)

# print(type(arr))

# Dimensions in Arrays
arr = np.array(42)
print(arr)

#2D array
arr2 = np.array([[1,2,3],[4,5,6]])
print("2D array: ",arr2)
print(arr2.shape) # gives the no of rows and no of columns

#3D array
arr3 = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print("3D array: ",arr3)
print(arr3.shape) #matrices #row #columns


# zeros array
zeros = np.zeros((3,4))
print("zeros array: \n", zeros)

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


