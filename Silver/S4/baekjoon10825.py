import sys
input = sys.stdin.readline
n=int(input())
arr=[]
for i in range(n):
    x=list(map(str,input().split()))
    arr.append(x)
arr.sort(key=lambda x:(-int(x[1]),int(x[2]),-int(x[3]),x[0]) )
for i in range(len(arr)):
    print(arr[i][0])