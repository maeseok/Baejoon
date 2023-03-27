import sys
#모듈 사용하여 리스트에 요소 추가 시 자동으로 최소 힙
import heapq
input = sys.stdin.readline
n=int(input())
heap=[]
for i in range(n):
    a=int(input().rstrip())
    if(a==0):
        try:
            #리스트의 가장 작은 값을 삭제 후 리턴
            print(heapq.heappop(heap))
        except:
            print(0)
    else:
        #(리스트,추가할 값)
        heapq.heappush(heap,a)