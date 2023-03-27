n=int(input())
arr=[1,1,2]
for i in range(3,n+1):
    tmp=0
    for j in range(i):
        tmp+=arr[j]*arr[i-j-1]
    arr.append(tmp)
print(arr[n])