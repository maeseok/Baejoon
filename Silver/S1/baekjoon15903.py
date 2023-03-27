import sys
input = sys.stdin.readline
n,m=map(int,input().split())
arr=list(map(int,input().split()))
arr.sort()
while m>0:
    x=arr[0]+arr[1]
    arr[0],arr[1]=x,x
    m-=1
    arr.sort()
print(sum(arr))