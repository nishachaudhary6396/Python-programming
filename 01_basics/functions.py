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