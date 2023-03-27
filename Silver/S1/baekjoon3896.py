import sys
input = sys.stdin.readline
n=1299709
dp=[False,False]+([True]*(n-1))
for i in range(2,n+1):
    for j in range(i*2,n+1,i):
        dp[j]=False

for _ in range(int(input())):
    k=int(input().rstrip())
    if(dp[k]):
        print(0)
    else:
        cnt=0
        for i in range(k,len(dp)):
            if dp[i]:
                break
            cnt+=1
        for j in range(k,-1,-1):
            if dp[j]:
                break
            cnt+=1
        print(cnt)