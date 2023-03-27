import sys
input = sys.stdin.readline
ans={}
for _ in range(int(input())):
    a=int(input())
    if(a not in ans):
        ans[a]=1
    else:
        ans[a]+=1
ans=sorted(ans.items(),key=lambda x:(-x[1],x[0]))
print(ans[0][0])