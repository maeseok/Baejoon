dp=[None]*41
dp[0]=[1,0]
dp[1]=[0,1]
t=int(input())
for i in range(t):
    a = int(input())
    if a==0 or a==1:
        print(*dp[a])
    else:
        for j in range(2,a+1):
            dp[j]=[dp[j-1][1],dp[j-1][0]+dp[j-1][1]]
        print(*dp[a])
            
'''
1 0 
0 1
1 1
1 2
2 3 
3 5 
5 8 
8 13
13 21 
21 34'''