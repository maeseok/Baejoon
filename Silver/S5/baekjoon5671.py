while True:
    try:
        a,b=map(int,input().split())
    except:
        break
    ans=0
    for i in range(a,b+1):
        tmp=set()
        i=str(i)
        for j in i:
            tmp.add(j)
        if len(tmp)==len(i):
            ans+=1
    print(ans)