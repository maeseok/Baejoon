n=int(input())
a=[None]*117
a[1],a[2],a[3]=1,1,1
for i in range(4,n+1):
    a[i]=a[i-1]+a[i-3]
print(a[n])