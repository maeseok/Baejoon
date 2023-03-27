import sys
T = int(sys.stdin.readline())
for _ in range(T):
    a,b = map(int,sys.stdin.readline().split())
    x = a*b
    #최소공배수 공식 기억
    while b>0:
        temp = a
        a =b
        b =temp%b
    print(x//a)