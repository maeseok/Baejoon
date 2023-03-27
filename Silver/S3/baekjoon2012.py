import sys
input = sys.stdin.readline
arr=[]
n=int(input())
for _ in range(n):
    arr.append(int(input().rstrip()))
#정렬 후에 각각 순서대로 등수 주는 것이 불만족도 가장 낮음
arr.sort()
res=0
for i in range(1,n+1):
    res+=abs(i-arr[i-1])
print(res)