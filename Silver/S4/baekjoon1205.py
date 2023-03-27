n,m,p = map(int,input().split())
if(n==0):
    print(1)
else: 
    arr=list(map(int,input().split()))
    if(p==n and arr[-1]>=m):
        print(-1)
    else:
        res = n+1
        for i in range(n):
            if arr[i]<=m:
                res=i+1
                break
        print(res)