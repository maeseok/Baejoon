from collections import deque
def sol():
    global cnt
    q=deque([n])
    while q:
        x=q.popleft()
        if x==k:
            cnt+=1
        for i in (x-1,x+1,2*x):
            if 0<=i<=10**5:
                if ans[i]==-1 or ans[i]==ans[x]+1:
                    ans[i]=ans[x]+1
                    q.append(i)
cnt=0
ans=[-1]*(10**5+1)
n,k=map(int,input().split())
ans[n]=0
sol()
print(ans[k])
print(cnt)