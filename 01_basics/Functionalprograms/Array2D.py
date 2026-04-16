#2D Array
m = int(input("Entr rows: "))
n = int(input("Enter columns: "))
arr = []
for i in range(m):
    row = []
    for j in range(n):
        val = int(input("Enter values: "))
        row.append(val)
    arr.append(row)

for i in range(m):
    for j in range(n):
        print(arr[i][j], end=" ")
    print()