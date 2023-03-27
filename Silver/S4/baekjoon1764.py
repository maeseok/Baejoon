#set을 사용해 집합으로 만들어서 교집합을 list형태로 저장
import sys
input = sys.stdin.readline
N,M = map(int,input().split())
a=set()
b=set()
for _ in range(N):
    a.add(input().rstrip())
for _ in range(M):
    b.add(input().rstrip())
result = list(a&b)
result.sort()
print(len(result))
for i in result:
    print(i)