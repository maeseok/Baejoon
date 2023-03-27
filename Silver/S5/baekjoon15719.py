n=int(input())
arr=list(map(int,input().split()))
for i in range(n):
    if(arr.count(i)==2):
        print(arr[i])
        break