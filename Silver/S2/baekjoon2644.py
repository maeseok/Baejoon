n=int(input())
a,b=map(int,input().split())
m=int(input())
dic={}
visited=[0]*(n+1)
res=[]
for i in range(n):
    dic[i+1]=set()
for i in range(m):
    x,y=map(int,input().split())
    dic[x].add(y)
    dic[y].add(x)

def dfs(v,num):
    num+=1
    visited[v]=1
    if v==b:
        res.append(num)
    for i in dic[v]:
        if not visited[i]:
            dfs(i,num)
dfs(a,0)
if len(res)==0:
    print(-1)
else:
    print(res[0]-1)
    