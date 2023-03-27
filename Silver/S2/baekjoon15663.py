n,m=map(int,input().split())
arr=sorted(list(map(int,input().split())))
tmp=[]
def dfs():
    global tmp
    if len(tmp)==m:
        for i in tmp:
            if tmp.count(i)>arr.count(i):
                return
        print(*tmp)
        return
    temp=0
    for i in range(len(arr)):
        if temp !=arr[i]:
            tmp.append(arr[i])
            temp=arr[i]
            dfs()
            tmp.pop()
dfs()