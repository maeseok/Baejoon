from collections import deque
n,m=map(int,input().split())
graph=[]
for _ in range(n):
    graph.append(list(map(int,input().split())))

def bfs(x,y):
    q=deque([(x,y)])
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    graph[x][y]=0
    cnt=1
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m and graph[nx][ny]==1:
                graph[nx][ny]=0
                cnt+=1
                q.append((nx,ny))
    return cnt
ans=[]
for i in range(n):
    for j in range(m):
        if graph[i][j]:
            ans.append(bfs(i,j))
if len(ans)==0:
    print(len(ans))
    print(0)
else:
    print(len(ans))
    print(max(ans))