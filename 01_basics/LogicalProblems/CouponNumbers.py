import random

n = int(input("Enter number of coupons: "))

collected = set()
count = 0

while len(collected) < n:
    num = random.randint(1, n)
    count += 1
    collected.add(num)   

print("Total picks:", count)