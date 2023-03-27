n,m = map(int,input().split())
a=list(map(int,input().split()))
a.sort()
ans=[]
def dfs():
    if(len(ans)==m):
        print(*ans)
        return
    for i in a:
        if i not in ans:
            ans.append(i)
            dfs()
            ans.pop()
dfs()