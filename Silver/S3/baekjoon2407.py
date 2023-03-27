import sys
input = sys.stdin.readline
n,m=map(int,input().split())
def factorial(n,m):
    ans=1
    cnt=0
    while cnt<m:
        ans*=n
        cnt+=1
        n-=1
    return ans
print(factorial(n,m)//factorial(m,m))