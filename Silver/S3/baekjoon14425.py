import sys
input =sys.stdin.readline
N,M = map(int,input().split())
arr=[]
arr2=[]
for _ in range(N):
    arr.append(input().rstrip())
for _ in range(M):
    arr2.append(input().rstrip())
cnt=0
for i in range(M):
    if(arr2[i] in arr):
        cnt+=1
print(cnt)