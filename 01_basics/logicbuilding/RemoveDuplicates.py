num = int(input("enter size : "))
arr = []
for i in range(num):
    arr.append(int(input("enter num : ")))

uniqueArr = []
for i in arr:
    if i not in uniqueArr:
        uniqueArr.append(i)

print(uniqueArr)