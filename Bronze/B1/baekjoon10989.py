import sys
input = sys.stdin.readline
N = int(input().rstrip())
#메모리 관리하기
N_list = [0]*10001
for i in range(N):
    N_list[int(input().rstrip())]+=1
for i in range(10001):
    if N_list[i] !=0:
        for j in range(N_list[i]):
            print(i)            