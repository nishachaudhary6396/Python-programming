# Q2:- Flip Coin and print percentage of Heads and Tails

import random
n = int(input("enter no of times to want to flip the coin : "))
h = 0
t = 0
for i in range(n):
    num = random.random()
    if num<0.5:
        t+=1
    else:
        h+=1
head_per = (h/n)*100
tail_per = (t/n)*100
print(f"percentage of heads: {head_per}% and percentage of tails: {tail_per}%")

