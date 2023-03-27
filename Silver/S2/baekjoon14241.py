n=int(input())
a=list(map(int,input().split()))
a.sort()
ans=0
while True:
    if len(a)==1:
        print(ans)
        break
    x=a.pop(0)
    y=a.pop(0)
    a.append(x+y)
    ans+=x*y
    a.sort()