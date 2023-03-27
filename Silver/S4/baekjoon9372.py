import sys
input = sys.stdin.readline 

def dfs(node,cnt):
    check[node]=1
    for n in graph[node]:
        if check[n]==0:
            cnt=dfs(n,cnt+1)
    return cnt
t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    graph = [[]for _ in range(n+1)]
    for _ in range(m):
        a,b=map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)
    check = [0]*(n+1)
    check[1]=0
    cnt=dfs(1,0)
    print(cnt)