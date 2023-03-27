n,m=map(int,input().split())
a = list(map(int,input().split()))
a.sort()
ans=[]
def dfs():
    if(len(ans)==m):
        print(*ans)
        return
    for i in a:
        if(len(ans)==0 or ans[-1]<=i):
            ans.append(i)
            dfs()
            ans.pop()
dfs()