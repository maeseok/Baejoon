#다이나믹 프로그래밍(dp) 문제는 점화식을 찾아야 하는게 관건
import sys
input = sys.stdin.readline
s=[]
n=int(input())
for i in range(n):
    s.append(int(input()))
dp=[0]*(n)
if(len(s)<=2):
    print(sum(s))
else:
    dp[0]=s[0]
    dp[1]=s[0]+s[1]
    for i in range(2,n):
        #계단 2개 연속 vs 1개 건너뛴 것 비교하여 값 갱신
        dp[i]=max(dp[i-3]+s[i-1]+s[i], dp[i-2]+s[i])
    print(dp[-1])
