num = int(input("enter size : "))
target = int(input("enter target : "))
arr = []
for i in range(num):
    arr.append(int(input("enter num : ")))

for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] + arr[j] == target:
            print(i, j)
            break
