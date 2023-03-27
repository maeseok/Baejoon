import sys
input = sys.stdin.readline
t=int(input())
for _ in range(t):
    ans=[]
    n=int(input())
    for i in range(2):
        ans.append(list(map(int,input().split())))
    for j in range(1,n):
        if j==1:
            ans[0][j] += ans[1][j-1]
            ans[1][j] += ans[0][j-1]
        else:
            ans[0][j] += max(ans[1][j-1], ans[1][j-2])
            ans[1][j] += max(ans[0][j-1], ans[0][j-2])
    print(max(ans[0][n-1], ans[1][n-1]))