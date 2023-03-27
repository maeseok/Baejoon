import sys
input = sys.stdin.readline
N=int(input())
arr = list(map(int,input().split()))
M=int(input())
max=max(arr)
min=1
while max>=min:
    mid=(max+min)//2
    res=0
    
    for i in arr:
        if mid<i:
            res+=mid
        else:
            res+=i
    if res>M:
        max=mid-1
    else:
        min=mid+1
print(max)