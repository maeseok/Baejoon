import sys
input = sys.stdin.readline
n=int(input())
a,b=map(int,input().split())
c=int(input())
arr=[]
for _ in range(n):
    arr.append(int(input()))
arr.sort(reverse=True)
tmp=[c,a]
ans=tmp[0]//tmp[1]
for i in range(len(arr)):
    x=tmp[0]+arr[i]
    y=tmp[1]+b
    if ans<=x//y:
        ans=x//y
        tmp[0]=x
        tmp[1]=y
    else:
        break
print(ans)