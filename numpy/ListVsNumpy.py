import numpy as np
import time

py_list = [1,2,3]
print("Pyhton list multiplication", py_list * 2) # list does not support mathematical operation

np_array = np.array([1,2,3])
print("Python array multiplication ", np_array * 2)

start = time.time()
py_list = [i*2 for i in range(100000000)]
print("\n List operation time: ", time.time() - start)

start = time.time()
np_array = np.arange(10000000) * 2
print("\n Numpy operation time: ", time.time() - start)
