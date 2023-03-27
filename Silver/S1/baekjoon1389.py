import sys
from collections import deque
input = sys.stdin.readline

n,m=map(int,input().split())
graph=[[] for _ in range(n+1)]
for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(s):
    tmp=[0]*(n+1)
    visited=[s]
    queue=deque([s])
    while queue:
        x=queue.popleft()
        for i in graph[x]:
            if i not in visited:
                tmp[i]=tmp[x]+1
                visited.append(i)
                queue.append(i)
    return sum(tmp)
ans=[]
for i in range(1,n+1):
    ans.append(bfs(i))
print(ans.index(min(ans))+1)