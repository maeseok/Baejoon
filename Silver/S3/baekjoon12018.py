n,m=map(int,input().split())
ans=[]
for _ in range(n):
    a,b=map(int,input().split())
    tmp=list(map(int,input().split()))
    tmp.sort(reverse=True)
    if a<b:
        ans.append(1)
    else:
        ans.append(tmp[b-1])
ans.sort()
sum=0
for i in range(len(ans)):
    sum+=ans[i]
    if sum>m:
        print(i)
        quit()
print(len(ans))