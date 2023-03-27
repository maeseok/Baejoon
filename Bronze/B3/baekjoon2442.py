N =int(input())
for i in range(1,N+1):
    X = 2*i-1
    Y = ((2*N-1)-X)//2
    print(" "*Y+"*"*X)