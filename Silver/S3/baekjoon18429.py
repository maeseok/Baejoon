n,m=map(int,input().split())
arr=list(map(int,input().split()))
ans=[]
cnt=0

def dfs(y):
    global cnt
    if(len(ans)==n):
        cnt+=1
        return
    for i in range(len(arr)):
        if(i not in ans):
            x=y-m+arr[i]
            if(x<500):
                continue
            else:
                ans.append(i)
                dfs(x)
                ans.pop()
dfs(500)  
print(cnt)