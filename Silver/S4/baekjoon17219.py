import sys
input = sys.stdin.readline
n,m=map(int,input().split())
ans=dict()
for _ in range(n):
    a,b=map(str,input().split())
    ans[a]=b
for i in range(m):
    x = input().rstrip()
    print(ans[x])