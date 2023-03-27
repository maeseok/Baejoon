import sys
from collections import deque
input = sys.stdin.readline
n,m=map(int,input().split())
def bfs(start):
    cnt=1
    queue=deque([start])
    visited=[0]*(n+1)
    visited[start]=True
    while queue:
        tmp=queue.popleft()
        for x in graph[tmp]:
            if not visited[x]:
                visited[x]=True
                cnt+=1
                queue.append(x)
    return cnt
graph=[[]for _ in range(n+1)]
for _ in range(m):
    a,b=map(int,input().split())
    graph[b].append(a)
max=1
ans=[]
for i in range(1,n+1):
    cnt=bfs(i)
    if cnt>max:
        max=cnt
        ans=[]
        ans.append(i)
    elif cnt==max:
        ans.append(i)
print(*ans)