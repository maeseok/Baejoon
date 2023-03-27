import sys
input = sys.stdin.readline
n,m=map(int,input().split())
tmp=[]
cnt=0
for i in range(n):
    tmp.append(input().rstrip())
for i in range(m):
    x=input().rstrip()
    for s in tmp:
        if s[:len(x)]==x:
            cnt+=1
            break
print(cnt)