dp=[None]*1000001
dp[0]=0
dp[1]=1
n=int(input())
if(n==0 or n==1):
    print(dp[n])
else:
    for i in range(2,n+1):
        dp[i]=(dp[i-1]+dp[i-2])%1000000007
    print(dp[n])