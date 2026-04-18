#find the largest number in an array

arr = [10, 25, 3, 67, 45]
large = arr[0]

for i in arr:
    if i > large:
        large = i

print(large)