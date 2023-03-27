import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6) 
n=int(input())
arr=list(map(int,input().split()))
x=int(input())
cnt=1
visited=[0]*(n+1)
def dfs(x):
    global cnt
    visited[x]=1
    for i in (x+arr[x], x-arr[x]):
        if 0<=i<n and visited[i]==0:
            cnt+=1
            visited[i]=1
            dfs(i)
dfs(x-1)
print(cnt)