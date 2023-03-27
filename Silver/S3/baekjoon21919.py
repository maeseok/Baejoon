n=1000000
arr=[False,False]+([True]*(n-1))
for i in range(2,n+1):
    if not arr[i]:
        continue
    for j in range(2*i,n+1,i):
        arr[j]=False
n=int(input())
a=set(list(map(int,input().split())))
ans=1
for i in a:
    if arr[i]:
        ans*=i
if ans==1:
    ans*=-1
print(ans)