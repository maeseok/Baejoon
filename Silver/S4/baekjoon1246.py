import sys
input = sys.stdin.readline
n,m=map(int,input().split())
arr=[]
for _ in range(m):
    arr.append(int(input().rstrip()))
arr.sort()
res=0
tmp=0
for i in range(len(arr)):
    if (len(arr)-i)<=n:
        y=(len(arr)-i)
    else:
        y=n
    x=arr[i]*y
    if res<x:
        res=x
        tmp=arr[i]
print(tmp, res)