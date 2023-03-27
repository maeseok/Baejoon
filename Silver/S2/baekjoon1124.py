a,b=map(int,input().split())

dp=[False,False]+([True]*(b-1))
for i in range(2,int(b**0.5)+1):
    for j in range(2*i,b+1,i):
        dp[j]=False
def sosu(n):
    tmp=0
    cnt=0
    x=n
    while x!=1:
        for i in range(2,x+1):
            if(x%i==0):
                x=x//i
                tmp+=1
                if dp[i]:
                    cnt+=1
                break
    if dp[cnt]:
        return True
    else:
        return False
ans=0
for i in range(a,b+1):
    if dp[i]==False:
        if sosu(i):
            ans+=1
print(ans)        