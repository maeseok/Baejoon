n,m=map(int,input().split())
arr=sorted(list(map(int,input().split())))
tmp=[]
def dfs(start):
    global tmp
    if len(tmp)==m:
        print(*tmp)
        return
    temp=0
    for i in range(start,len(arr)):
        if temp !=arr[i]:
            tmp.append(arr[i])
            temp=arr[i]
            dfs(i)
            tmp.pop()
dfs(0)