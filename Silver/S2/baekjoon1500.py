s,k=map(int,input().split())
q=s//k
r=s%k
ans=1
while k>0:
    if r>0:
        ans*=q+1
        r-=1
    else:
        ans*=q
    k-=1
print(ans)