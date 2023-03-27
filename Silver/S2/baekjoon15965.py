n=int(input())
ans=[]
x=10**7
dp=[False,False]+([True]*x)
for i in range(2,x+1):
    if dp[i]:
        ans.append(i)
        if(len(ans)==n):
            print(ans[-1])
            quit()
        for j in range(i*2,x+1,i):
            dp[j]=False