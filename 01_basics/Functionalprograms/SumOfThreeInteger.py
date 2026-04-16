# sum of threee adds to zero
n = int(input("Enter the arrayyy size:"))
arr = []
for i in range(n):
    ele = int(input("Enter element: "))
    arr.append(ele)

count=0
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if arr[i]+arr[j]+arr[k] ==0:
                print(arr[i],arr[j],arr[k])
                count+=1
print("total",count)
