from collections import deque
t=int(input())
def bfs(x,y):
    graph[x][y]="."
    q=deque([(x,y)])
    while q:
        x,y=q.popleft()
        dx=[-1,1,0,0]
        dy=[0,0,-1,1]
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<h and 0<=ny<w and graph[nx][ny]=="#":
                q.append((nx,ny))
                graph[nx][ny]="."
for _ in range(t):
    h,w=map(int,input().split())
    graph=[]
    for _ in range(h):
        graph.append(list(input()))
    ans=0
    for i in range(h):
        for j in range(w):
            if graph[i][j]=="#":
                bfs(i,j)
                ans+=1
    print(ans)