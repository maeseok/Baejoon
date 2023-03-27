import sys
T =int(input())
#최단거리 공식 알면 가능
for _ in range(T):
    List = list(map(int,sys.stdin.readline().split()))
    a = max(List)
    List.remove(a)
    print(a**2+sum(List)**2)