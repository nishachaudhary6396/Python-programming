import numpy as np

arr = np.array([5, 2, 9, 1])
sorted_arr = np.sort(arr)
print(sorted_arr)

#in 2D array
arr = np.array([[3, 1, 2],
                [6, 4, 5]])

print(np.sort(arr))

#Descending order sorting
arr = np.array([5, 2, 9, 1])
print(np.sort(arr)[::-1])