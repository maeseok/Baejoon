n=int(input())
dp=[float(input()) for _ in range(n)]
for i in range(1,n):
    dp[i]=max(dp[i-1]*dp[i],dp[i])
print("{:.3f}".format(max(dp)))