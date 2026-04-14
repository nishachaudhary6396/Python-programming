#harmonic numbers
N = int(input("enter a number : "))
if N==0:
    print("n should not be zero")
else:
    harmonic = 0
    for i in range(1,N+1):
        harmonic += 1/i

    print("Harminic value is : ",harmonic)
