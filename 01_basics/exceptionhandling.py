# exception handling is the process of handling unwanted or unexpected errors ocuredwhen the code runs

a = input("Enter the number: ")
print(f"Multiolication table of {a} is: ")
try:
    for i in range(1,11):
        print(f"{int(a)} * {i} = {int(a)*i}")
#except Exception as e:
except:
    print("what you done!!! correct thiss")
print("This is Nisha")
print("placed in apaxon")

# Another example
try:
    num = int(input("enter a number:"))
    a = [4,5,6]
    print(a[5])
except ValueError:
    print("Number is not valid")
except IndexError:
    print("Index Error")
finally:
    print("always run")