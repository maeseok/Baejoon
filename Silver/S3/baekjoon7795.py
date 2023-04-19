for _ in range(int(input())):
    ans=0
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    b.sort()
    for i in range(n):
        if a[i]<=b[0]:
            continue
        elif a[i]>b[m-1]:
            ans+=m
        else:
            start=0
            end=m-1
            while start+1<end:
                mid=(start+end)//2
                if a[i]>b[mid]:
                    start=mid
                else:
                    end=mid
            ans+=end
    print(ans)