#heapq를 모름 -> 최소힙 사용 
# 정렬된 상태로 추가되고 삭제됨
import sys
import heapq
input = sys.stdin.readline
n=int(input())
heap = []

for _ in range(n):
    a=int(input())
    if(a==0):
        if heap:
            print(-1*heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap,(-a))