import sys
input = sys.stdin.readline
for _ in range(int(input())):
    k=int(input())
    n=int(input())
    f0=[x for x in range(1,n+1)]
    for u in range(k):
        for i in range(1,n):
            f0[i]+=f0[i-1]
    print(f0[-1])