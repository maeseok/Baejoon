import sys
input = sys.stdin.readline
n=int(input())
ans={}
for i in range(n):
    a,b = map(str,input().rstrip().split('.'))
    if b in ans:
        ans[b]+=1
    else:
        ans[b]=1
ans=sorted(ans.items(),key=lambda x:x[0])
for i in ans:
    print(i[0] ,i[1])