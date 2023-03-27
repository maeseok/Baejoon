#틀림
import sys
N = int(sys.stdin.readline().rstrip())
sum=0
List = list(map(int,sys.stdin.readline().split()))
List.sort()
N=len(List)
for i in range(N):
    sum += List[i]*(2*i-N+1)
print(sum*2)