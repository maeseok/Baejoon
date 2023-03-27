import sys
input = sys.stdin.readline
n=int(input())
arr=[]
for _ in range(n):
    arr.append(int(input()))
arr.sort(reverse=True)
x=n//3
ans=sum(arr)
for i in range(2,n,3):
    ans-=arr[i]
print(ans)