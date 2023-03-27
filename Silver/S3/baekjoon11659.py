import sys
input = sys.stdin.readline
n,m=map(int,input().split())
arr=list(map(int,input().split()))
prefix_sum=[0]

#배열 구간의 합을 미리 구해 시간 복잡도 낮춤
temp=0
for i in arr:
    temp+=i
    prefix_sum.append(temp)

for _ in range(m):
    sum=0
    a,b = map(int,input().split())
    print(prefix_sum[b]-prefix_sum[a-1])