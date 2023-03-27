from collections import deque
n,m=map(int,input().split())
graph=[]
q=deque()
for i in range(n):
    tmp=list(map(int,input().split()))
    for j in range(m):
        if tmp[j]==1:
            q.append((i,j))
    graph.append(tmp)

def bfs():
    dx=[-1,1,0,0,-1,1,-1,1]
    dy=[0,0,-1,1,1,-1,-1,1]
    while q:
        x,y=q.popleft()
        for i in range(8):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if graph[nx][ny]==0:
                    q.append((nx,ny))
                    graph[nx][ny]=graph[x][y]+1
    return
bfs()
ans=0
for i in range(n):
    for j in range(m):
        ans=max(graph[i][j],ans)
print(ans-1)