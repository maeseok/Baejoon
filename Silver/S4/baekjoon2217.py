import sys
input = sys.stdin.readline
List=[]
value=[]
N=int(input())
for i in range(N):
    List.append(int(input()))
List.sort(reverse=True)
for num in range(N):
    value.append(List[num]*(num+1))
print(max(value))