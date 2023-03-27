def gcd(a,b):
    while b>0:
        a,b = b, a%b
    return a

t=int(input())
for i in range(t):
    a=list(map(int,input().split()))
    a=a[1:]
    ans=0
    for i in range(len(a)):
        for j in range(i+1,len(a)):
                ans+=gcd(a[i],a[j])
    print(ans)