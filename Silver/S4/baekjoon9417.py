def gcd(a,b):
    while b:
        mod=b
        b=a%b
        a=mod
    return a
    
for _ in range(int(input())):
    x=list(map(int,input().split()))
    ans=0
    for i in range(len(x)):
        for j in range(len(x)):
            if i!=j and i>j:
                ans=max(gcd(x[i],x[j]),ans)
    print(ans)