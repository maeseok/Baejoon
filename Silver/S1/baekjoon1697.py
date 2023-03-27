from collections import deque

def sol():
    q=deque([n])
    while q:
        x=q.popleft()
        if x==k:
            return ans[x]
        for i in (x-1,x+1,2*x):
            if 0<=i<=10**5 and not ans[i]:
                ans[i]=ans[x]+1
                q.append(i)
ans=[0]*(10**5+1)
n,k=map(int,input().split())
print(sol())