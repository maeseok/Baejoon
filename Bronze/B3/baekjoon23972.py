K,N = map(int,input().split())
if(N==1):
    print(-1)
else:
    x =N*K//(N-1)
    if(N*K)%(N-1):
        x+=1
    print(x)