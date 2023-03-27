from collections import deque
n=int(input())
graph=[]
for i in range(n):
    graph.append(list(map(int,input())))

def bfs(x,y):
    dx=[0,0,-1,1]
    dy=[-1,1,0,0]
    q=deque([(x,y)])
    graph[x][y]=0
    cnt=1
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n and graph[nx][ny]==1:
                graph[nx][ny]=0
                q.append((nx,ny))
                cnt+=1
    return cnt
ans=[]
for i in range(n):
    for j in range(n):
        if graph[i][j]==1:
            ans.append(bfs(i,j))
ans.sort()
print(len(ans))
print(*ans,sep="\n")

        