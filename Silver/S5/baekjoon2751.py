import sys
N=int(sys.stdin.readline().rstrip())
List=[]
for _ in range(N):
    List.append(int(sys.stdin.readline().rstrip()))
List.sort()
for i in List:
    print(i)