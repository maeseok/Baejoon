import sys
N = int(input())
x =0
List=[]
for i in range(N):
    List=list(map(int,sys.stdin.readline().split()))
    for j in range(len(List)):
        x+=int(List[j])
print(x)