n=int(input())
dp=[None]*33334
dp[1]=0
dp[2]=2
for i in range(3,n+1):
    dp[i]=dp[i-1]*3%1000000009
print(dp[n])