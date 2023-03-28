n=int(input())
tmp=list(map(int,input().split()))
tmp.sort()
ans=tmp.pop()
for i in tmp:
    ans+=i/2
print(ans)