L,R,A = map(int,input().split())
x = min(L,R)
y = max(L,R)
if(L==R):
    print((L+A//2)*2)
else:
    if(x+A <=y):
        print((x+A)*2)
    else:
        A =(x+A)-y
        print(y*2+A//2*2)