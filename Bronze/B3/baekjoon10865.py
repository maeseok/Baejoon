import sys
N,M=map(int,sys.stdin.readline().split())
List=[]
for i in range(1,N+1):
    List.append(i)
for _ in range(M):
    a,b=map(int,sys.stdin.readline().split())
    List[a-1] +=1
    List[b-1] +=1
for i in range(1,N+1):
    print(List[i-1]-i)