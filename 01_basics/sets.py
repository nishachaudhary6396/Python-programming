#  set is unordered, mutable, does not allow duplicate values, heterogenous, represented by {}, does not support indexing
set = {1,2,3,4,5}
print(set)
set_var = {"nisha","chaudhary","learning","python"}
print(set_var)
print(type(set_var))
set.add("help")
print(set)
set1 = {"nisha","chaudhary","learning","python"}
set2 = {"nisha","chaudhary","learning"}
print(set1.difference(set2))
print(set2.intersection(set1))
