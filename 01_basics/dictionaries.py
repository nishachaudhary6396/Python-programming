# A dictionaries is a collection of items which is unordered,mutable,allow duplicate values, changeable, written with curly braces and has key value
my_dict = {"name":"nisha","age":22,"city":"Agra"}
print(my_dict)
print(type(my_dict))
print(my_dict['name'])
for x in my_dict:
    print(x)
for i in my_dict.values():
    print(i)
for i in my_dict.items():
    print(i)

# adding items in dictionaries
my_dict['car'] = 'BMW'
print(my_dict)


# nested dictionaries
car1 = {"brand":"BMW","year":2025}
car2 = {"brand":"Audi","year":2022}
car3 = {"brnad":"defender","year":2023} 

car_type={"car1":car1,"car2":car2,"car3":car3}
print(car_type)