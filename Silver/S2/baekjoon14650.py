N=int(input())
ans=0
def dfs(n,sum):
    global ans
    print(n,sum)
    for i in range(3):
        if n==0 and i==0:
            continue
        if n==N:
            if sum%3==0:
                ans+=1
                print(ans)
                return ans
        else:
            dfs(n+1,sum+i)
dfs(0,0)
print(ans)b