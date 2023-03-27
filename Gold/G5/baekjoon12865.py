n,k=map(int,input().split())
arr=[[0,0]]
ans=[[0 for _ in range(k+1)] for _ in range(n+1)]
for _ in range(n):
    arr.append(list(map(int,input().split())))

for i in range(1,n+1):
    for j in range(1,k+1):
        weight=arr[i][0]
        value=arr[i][1]
        
        if j<weight:
            ans[i][j]=ans[i-1][j]
        else:
            ans[i][j]=max(value+ans[i-1][j-weight],ans[i-1][j])
print(ans[n][k])