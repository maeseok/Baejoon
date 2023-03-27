n=int(input())
arr=list(map(int,input().split()))
arr.sort(reverse=True)
tmp=1
ans=0
for i in arr:
    ans=max(ans,tmp+i)
    tmp+=1
print(ans+1)