from collections import deque
import sys
input = sys.stdin.readline
def bfs(graph,x,y):
    q=deque([(x,y)])
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    graph[x][y]=0
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m and graph[nx][ny]==1:
                q.append((nx,ny))
                graph[nx][ny]=0
    return
T=int(input())
for _ in range(T):
    n,m,k=map(int,input().split())
    graph=[[0]*(m) for _ in range(n)]
    for _ in range(k):
        a,b=map(int,input().split())
        graph[a][b]=1
    cnt=0
    for i in range(n):
        for j in range(m):
            if graph[i][j]==1:
                bfs(graph,i,j)
                cnt+=1
    print(cnt)


    