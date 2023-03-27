import sys
Q = int(input())
for j in range(Q):
    a = int(sys.stdin.readline())
    if((a&(-a))==a):
        print(1)
    else:
        print(0)