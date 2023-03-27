cnt=1
while True:
    ans=0
    l,p,v = map(int,input().split())
    if l==p==v==0:
        break
    x=v//p
    ans+=l*x
    if v%p<=l:
        ans+=v%p
        print("Case "+str(cnt)+": "+str(ans))
    else:
        ans+=l
        print("Case "+str(cnt)+": "+str(ans))
    cnt+=1