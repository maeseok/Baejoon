import sys
T=int(input())
for _ in range(T):
    A=0
    B=0
    N=int(sys.stdin.readline())
    for _ in range(N):
        a,b = map(str,sys.stdin.readline().split())
        A +=int(a)
        B+=int(a)*float(b)
    print(A, '{:.1f}'.format(B/A))