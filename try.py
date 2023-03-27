n,k=map(int,input().split())
if(n>k):
    print(n-k)
else:
    while n<=k:
        n*=2
        if(n>k):
            
        