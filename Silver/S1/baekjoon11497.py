import sys
input = sys.stdin.readline
n=int(input())
for _ in range(n):
    x=int(input())
    arr=list(map(int,input().split()))
    arr.sort()
    res=0
    for i in range(2,x):
        #그리디 핵심
        res=max(res,abs(arr[i]-arr[i-2])) 
    print(res)       