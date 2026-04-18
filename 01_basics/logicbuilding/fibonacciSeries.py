#fibonacci series

n = int(input("enter num : "))
a, b = 0, 1

for i in range(n):
    print(a)
    a, b = b, a + b

