import sys
input = sys.stdin.readline
List=[]
for _ in range(int(input())):
    a = list(map(int,input().split()))
    List.append(a)
List.sort()
for i in List:
    print(*i)