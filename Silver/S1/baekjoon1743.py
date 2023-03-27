import sys
from collections import deque
n,m,k=map(int,input().split())
graph=[[0 for _ in range(m+1)] for _ in range(n+1)]
for _ in range(k):
    a,b=map(int,input().split())
    graph[a][b]=1
    
def bfs(x,y):
	#01
    ans=1
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    q=deque([(x,y)])
    graph[x][y]=2
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<nx<=n and 0<ny<=m and graph[nx][ny]==1:
                q.append((nx,ny))
                graph[nx][ny]=2
                ans+=1
    return ans
answer=0
for i in range(1,n+1):
    for j in range(1,m+1):
        if graph[i][j]==1:
            ans=bfs(i,j)
            answer=max(answer,ans)
print(answer)