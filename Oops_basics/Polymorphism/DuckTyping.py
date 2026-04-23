# waht is duck typing ->
# python does not care about about the class and type ...it only cares whether the object has the required method

class Dog:
    def sound(self):
        print("Barkkkkkk")
class cat:
    def sound(self):
        print("meeeeowwwww")
def make_sound(obj):
    obj.sound()

make_sound(Dog())
make_sound(cat())


# polymorphism in Operators->
# same operators beahe different task depending on the operand types.

print(5 + 6)  
print("Nisha" + "Chaudhary")
print([1,2]+[3,4,5])