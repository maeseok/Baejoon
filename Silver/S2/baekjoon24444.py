from collections import deque
import sys
input = sys.stdin.readline
n,m,r=map(int,input().split())
graph=[[] for _ in range(n+1)]
visited=[0]*(n+1)
for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def vfs(v):
    queue=deque([v])
    visited[v]=1
    cnt=2
    while queue:
        x=queue.popleft()
        graph[x].sort()
        for i in graph[x]:
            if not visited[i]:
                visited[i]=cnt
                cnt+=1
                queue.append(i)
vfs(r)
for i in visited[1:]:
    print(i)
