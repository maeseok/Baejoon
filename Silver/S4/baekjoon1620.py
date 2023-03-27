#딕셔너리 사용하여, 시간복잡도 낮춤
import sys
input = sys.stdin.readline
N,M=map(int,input().split())
arr=dict()
arr2=dict()
x=[]
for i in range(1,N+1):
    name = input().rstrip()
    arr[str(i)] = name
    arr2[name] = i
for _ in range(M):
    x.append(input().rstrip())

for i in range(len(x)):
    if(x[i] in arr):
        print(arr[x[i]])
    else:
        print(arr2[x[i]])