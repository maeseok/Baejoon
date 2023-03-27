from collections import deque
n=int(input())
m=int(input())
graph=[[]*(n+1) for _ in range(n+1)]
visited=[0]*(n+1)
for i in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(v):
    queue=deque([v])
    visited[v]=1
    while queue:
        x=queue.popleft()
        for i in graph[x]:
            if not visited[i]:
                print(visited)
                queue.append(i)
                visited[i]=visited[x]+1
dfs(1)
res=0
for i in range(2,n+1):
    if visited[i]<4 and visited[i]!=0:
        res+=1
print(res)