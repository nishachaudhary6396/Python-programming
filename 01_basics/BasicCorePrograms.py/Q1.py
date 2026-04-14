# Q1:- User Input and Replace String Template "Hello<<UserName>>, How are you?"

name = input("Enter name :")
if len(name)<3:
    print("Name should have min 3 char")
else:
    print(f"Hello {name}, How are you?")
