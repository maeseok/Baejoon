a,b=map(int,input().split())
B=max(a,b)
A=min(a,b)
tmp=B-A-1
if tmp<=0:
    print(0)
else:
    print(tmp)
    for i in range(A+1,B):
        print(i,end=" ")