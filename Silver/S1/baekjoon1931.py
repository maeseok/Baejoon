import sys
input = sys.stdin.readline
n=int(input())
tmp=[]
for _ in range(n):
    tmp.append(list(map(int,input().split())))
tmp.sort(key=lambda x:(x[1],x[0]))
print(tmp)
ans,end=0,0
for a,b in tmp:
    if a>=end:
        ans+=1
        end=b
print(ans)