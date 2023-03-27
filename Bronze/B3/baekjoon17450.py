s1,s=map(int,input().split())
n1,n=map(int,input().split())
u1,u=map(int,input().split())
S=(s*10)/(10*s1-500 if 10*s1>=5000 else 10*s1)
N=(n*10)/(10*n1-500 if 10*n1>=5000 else 10*n1)
U=(u*10)/(10*u1-500 if 10*u1>=5000 else 10*u1)
if(max(S,N,U)==S):
    print("S")
elif(max(S,N,U)==N):
    print("N")
else:
    print("U")