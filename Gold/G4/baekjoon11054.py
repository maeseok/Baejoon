n=int(input())
a=list(map(int,input().split()))
plus= [1 for i in range(n)]

for i in range(n):
    for j in range(i):
        if a[i]>a[j]:
            plus[i]=max(plus[i],plus[j]+1)

minus=[1 for i in range(n)]
for i in range(n-1,-1,-1):
    for j in range(n-1,i,-1):
        if a[i]>a[j]:
            minus[i]=max(minus[i],minus[j]+1)

ans=[0]*n
for i in range(n):
    ans[i]=plus[i]+minus[i]-1
print(max(ans))