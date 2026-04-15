def hello():
    print("hello world")
hello() 

def sum(a,b):
    print(f"the sum of your numbers is {a + b}")

sum(2,3)

# Question by using a palindrome number->

def palindrome(st):
    rev = "" 
    for i in range(len(st)-1,-1,-1):
        rev = rev + st[i]
    if st ==rev:
        print("palindrome")
    else:
        print("not palindrome")

def is_print():
    print("hello nisha")
is_msg = is_print()
print(is_msg)

def is_return():
    return "hello gurlll"
is_msg2 = is_return()
print(is_msg2)

def login():
    pass    # if you dont have anything to write leave as pass


