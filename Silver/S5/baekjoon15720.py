b,c,d=map(int,input().split())
x=min(b,c,d)
B=list(map(int,input().split()))
B.sort(reverse=True)
C=list(map(int,input().split()))
C.sort(reverse=True)
D=list(map(int,input().split()))
D.sort(reverse=True)
ans=sum(B)+sum(C)+sum(D)
tmp=0
for i in range(x):
    tmp+=B[i]+C[i]+D[i]
print(ans)
print(ans-int(tmp*0.1))