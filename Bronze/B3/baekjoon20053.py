import sys
T = int(input())
for _ in range(T):
    N = int(input())
    List = list(map(int,sys.stdin.readline().split()))
    print(min(List) ,max(List)) 