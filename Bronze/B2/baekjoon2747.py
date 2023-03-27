dp=[None]*46
dp[0]=0
dp[1]=1
x = int(input())
if (x<2):
    print(dp[x])
else:
    for i in range(2,x+1):
        dp[i]=dp[i-1]+dp[i-2]
    print(dp[x])