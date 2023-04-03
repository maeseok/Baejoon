n,m=map(int,input().split())
a=set(map(int,input().split()))
b=set(map(int,input().split()))
ans=[]
for i in a:
    if i not in b:
        ans.append(i)
ans.sort()
print(len(ans))
if len(a)!=0:
    print(*ans)