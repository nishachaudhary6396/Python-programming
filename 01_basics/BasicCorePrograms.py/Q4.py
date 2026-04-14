# Power of 2

N = int(input("Enter value of N: "))

if N < 0 or N >= 31:
    print("Enter value btw 0 and 31")
else:
    for i in range(N + 1):
        print("2^", i, "=", 2 ** i)