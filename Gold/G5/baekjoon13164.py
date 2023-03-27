n,k=map(int,input().split())
arr=list(map(int,input().split()))
ans=[]
for i in range(1,n):
    ans.append(arr[i]-arr[i-1])
ans.sort(reverse=True)
print(sum(ans[k-1:]))