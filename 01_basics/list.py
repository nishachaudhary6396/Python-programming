# list is a collection of items that is mutable,ordered,allow duplicate values, heterogenous

fruits = ["apple", "banana", "guava"]

a = [12,13,23,34,45,True,34.6]
print(len(a))
print(a[0],a[5])

# list methods->
a = [1,2,3,4,5,6]
a.append(7)
print(a)
a.insert(2,8)
print(a)
a.extend([9,10])
print(a)
a.remove(2)
print(a)
a.reverse()
print(a)
a.pop(0)
print(a)
a.count(3)  # total occurences of the element
print(a)

