import sys
T = int(input())
for _ in range(T):
    List = list(map(int,sys.stdin.readline().split()))
    HP = List[0] + List[4]
    MP = List[1] + List[5]
    at = List[2] + List[6]
    de = List[3] + List[7]
    print((HP if HP>=1 else 1)+5*(MP if MP>=1 else 1)
    +2*(at if at>=0 else 0)+2*de)