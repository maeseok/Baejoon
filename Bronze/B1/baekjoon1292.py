a,b=map(int,input().split())
cnt=1
ans=[]
for i in range(1,b+1):
    for j in range(cnt):
        ans.append(i)
    if len(ans)>=b:
        break
    cnt+=1
print(sum(ans[a-1:b]))