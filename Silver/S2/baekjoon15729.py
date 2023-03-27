n=int(input())
arr=list(map(int,input().split()))
tmp=[False]*n
cnt=0
for i in range(n):
    if arr[i]!=tmp[i]:
        cnt+=1
        tmp[i]=not tmp[i]
        if i+1<n:
            tmp[i+1]=not tmp[i+1]
        if i+2<n:
            tmp[i+2]=not tmp[i+2]
print(cnt)