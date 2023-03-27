import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n,m,r=map(int,input().split())
graph=[[] for _ in range(n+1)]
visited=[0]*(n+1)
for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(v):
    global cnt
    visited[v]=cnt
    graph[v].sort(reverse=True)
    for i in graph[v]:
        if not visited[i]:
            cnt+=1
            dfs(i) 
cnt=1
dfs(r)
for i in visited[1:]:
    print(i)