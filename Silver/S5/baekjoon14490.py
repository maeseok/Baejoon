def gcd(a,b):
    while b>0:
        a,b=b,a%b
    return a
a=list(map(int,input().split(":")))
x=gcd(a[0],a[1])
a[0]=a[0]//x
a[1]=a[1]//x
a[0]=str(a[0])
a[1]=str(a[1])
print(":".join(a))