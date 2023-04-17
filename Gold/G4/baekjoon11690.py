n=int(input())
tmp=[False,False]+([True]*(n-1))
for i in range(2,int(n**0.5)+1):
    if tmp[i]:
        for j in range(2*i,n+1,i):
            tmp[j]=False

ans=1
for i in range(2,len(tmp)-1):
    if tmp[i]:
        temp=1
        while temp*i<=n:
            temp*=i
        ans=ans*temp
print(ans%2**32)