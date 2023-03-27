N,W,H,L = map(int,input().split())

x = (W//L)*(H//L)
if(x>=N):
    print(N)
else:    
    print(x)