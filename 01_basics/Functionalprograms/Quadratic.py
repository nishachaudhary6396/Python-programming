# Ouadratic Questions:-
# Write a code to dindd the roots of the Quadratic Questions

a = int(input("enter a value: "))
b = int(input("enter b value: "))
c = int(input("enter c value: "))
d = b**2-4*a*c
if d<0:
     print("No real roots")
else:
    root1 = (-b + d**0.5) / (2*a)
    root2 = (-b - d**0.5) / (2*a)
    print("Root 1:", root1)
    print("Root 2:", root2)