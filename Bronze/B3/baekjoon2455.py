on=[]
ans=0
for _ in range(4):
    a,b=map(int,input().split())
    ans+=b
    ans-=a
    on.append(ans)
print(max(on))