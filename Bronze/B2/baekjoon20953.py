import sys
T=int(sys.stdin.readline())
for i in range(T):
    a,b = map(int,sys.stdin.readline().split())
    n = a+b
    print((n)*(n-1)*(n)//2)