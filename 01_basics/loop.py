# for loop->

for i in range(1,11,2):
    print(i)
for i in range(20,51):
    print(i)
for i in range(16,0,-1):
    print(i)

n = int(input("write table : "))
for i in range(n, (n*10)+1,n):
    print(i)

a = "SHERYIANS TEACHES INDUSTRY THINGS"
print(len(a))
for i in range(len(a)):
      print(a[i])

a = "SHREYINS IS COOL"
for i in a:
    print(i)

for i in range(1,21):
     if i == 15:
         break
     else:
         print(i)

# for loop questions->

n = int(input("enter a number: "))
for i in range(n):
    print("hello world")

n = int(input("enter a number: "))
for i in range(n,0,-1):
    print(i)

n = int(input("enter a number: "))
for i in range(1,11):
    print(f"{n} * {i} = {n*i}")

# sum of n natural numbers->
n = int(input("enter a number: "))
sum = 0
for i in range(1,n+1):
    sum = sum + i
    print(f"your sum is {sum}")

#  factorial ->
n = int(input("enter a number:"))
fact = 1
for i in range(1,n+1):
    fact = fact * i

print(f"factorial is {fact} ")


# sum of even and odd numbers->
n = int(input("enter a number: "))
even = 0
for i in range(1,n+1):
    if i%2==0:
       even = even + i
    else:
        odd = odd + i


#perfect number->
n = int(input("please tell your number : "))
sum = 0
for i in range(1,n):
    if n%i ==0:
       sum = sum+i
    if sum == n:
       print("your number is perfect")
    else:
       print("not a perfect number")

#prime numbers->
n = int(input("enter a number: "))
count = 0
for i in range(1,n+1):
    if n%i==0:
        count = count+1
if count ==2:
    print("prime number")
else:
    print("not A Prime numberr")

#reverse->
a = "Nisha"
for i in range(4,-1,-1):
    print(a[i])

#palindrome->
a = "Nisha"
b = ""
for i in range(len(a)-1,-1,-1):
    b = b+ a[i]
if a ==b:
    print("palindrome")
else:
    print("not a palindrome")

# while loop->
a = 1
while a<=10:
    print(a)
    a = a+1










