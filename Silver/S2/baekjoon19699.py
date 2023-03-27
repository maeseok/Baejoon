def dfs(start,depth,sum):
    if depth==m:
        if sum in prime:
            ans.add(sum)
    for i in range(start,n):
        if not visited[i]:
            visited[i]=True
            dfs(i+1,depth+1,sum+x[i])
            visited[i]=False

n=9000
prime=[]
tmp=[False,False]+([True]*(n-1))
for i in range(2,n):
    if tmp[i]:
        prime.append(i)
    for j in range(2*i,n-1,i):
        tmp[j]=False
n,m=map(int,input().split())
x=list(map(int,input().split()))
visited=[False]*n
ans=set()
dfs(0,0,0)
if ans:
    print(*sorted(list(ans)))
else:
    print(-1)