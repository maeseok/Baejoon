import sys
input = sys.stdin.readline
while True:
    n,k=map(int,input().split())
    if n==0 and k==0:
        break
    ans=1
    tmp=1
    for i in range(n,max(k,n-k),-1):
        ans*=i
    for i in range(2,min(n-k,k)+1):
        tmp*=i
    print(ans//tmp)