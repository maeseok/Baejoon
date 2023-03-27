#heapq을 알아야 함
import heapq
import sys
input = sys.stdin.readline
q=[]
n=int(input())
for i in range(n):
    a = int(input().rstrip())
    if a!=0:
        #절댓값,원래값 -> 절대값 순으로 정렬
        heapq.heappush(q,(abs(a),a))
    else:
        if not q:
            print(0)
        else:
            #첫번째 값은 음수화한 값 두번째 값은 원래 값
            #즉 인덱스 1인 원래 값을 출력
            print(heapq.heappop(q)[1])