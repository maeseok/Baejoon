import sys
input = sys.stdin.readline
n=int(input())
arr=list(map(int,input().split()))
arr.sort(reverse=True)
tmp=arr[0]
res=0
for i in range(len(arr)):
    if i==0:
        pass
    else:
        res+=tmp+arr[i]
print(res)