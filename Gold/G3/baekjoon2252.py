from collections import deque
n,m=map(int,input().split())
graph=[[] for _ in range(n+1)]
tmp=[0 for _ in range(n+1)]
q=deque()
ans=[]
for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    tmp[b]+=1
for i in range(1,n+1):
    if tmp[i]==0:
        q.append(i)
while q:
    x=q.popleft()
    ans.append(x)
    for i in graph[x]:
        tmp[i]-=1
        if tmp[i]==0:
            q.append(i)
print(*ans)