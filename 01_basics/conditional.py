if a>10:
    print("true")
else:
    print("false")


#which num is greater->
num1 = int(input("enter first number : "))
num2 = int(input("enter second number : "))
if num1 > num2:
    print("num1 is greater")
else:
    print("num2 is greater")

#2->
gen = input("please tell your gender as character : ")
if gen == 'M':
    print("Good Morning sir")
elif gen == 'F':
    print("Good Morning Mam")
else:
    print("unidentified gender")


#3->
num = int(input("enter a number :"))
if num%2 ==0:
    print("even")
else:
    print("odd")


#if,else,elif
year = int(input("Enter a year :"))
if year % 100 == 0 and year % 400 ==0:
    print("Leap year")
elif year % 100 != 0 and year % 4 ==0:
    print("Leap year")
else:
    print("its a normal year")

