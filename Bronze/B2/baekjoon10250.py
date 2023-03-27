import sys
input = sys.stdin.readline
T=int(input())
for _ in range(T):
    H,W,N = map(int,input().split())
    y=N//H+1
    X=N%H
    if(X==0):
        y-=1
        X=H
    answer = str(X)+str("{0:02d}".format(y))
    print(answer)