import sys
input = sys.stdin.readline
t=int(input())
for _ in range(t):
    ans=0
    max=0
    a=int(input())
    arr=list(map(int,input().split()))
    for i in range(len(arr)-1,-1,-1):
        if arr[i]>max:
            max=arr[i]
        else:
            ans+=max-arr[i]
    print(ans)