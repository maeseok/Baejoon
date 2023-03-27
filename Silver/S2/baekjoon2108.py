import sys
import math
input = sys.stdin.readline
arr=[]
cnt=[0]*4000
answer=[]
n=int(input())
for _ in range(n):
    arr.append(int(input()))
arr.sort()
avg="{:.0f}".format(sum(arr)/len(arr))
#평균
if(avg=="-0"):
    print(0)
else:
    print(int(avg))
#중앙값
print(arr[math.ceil(n/2)-1])
#최빈값
counts=dict()
for i in range(1,n+1):
    counts[i]=[]
maxCount=1
count=1
for j in range(1,n):
    if arr[j] == arr[j-1]:
        count+=1
    else:
        counts[count].append(arr[j-1])
        if maxCount < count: maxCount=count
        count=1
    if j ==n-1:
        counts[count].append(arr[j])
        if maxCount<count:maxCount=count
if n==1:
    counts[1].append(arr[0])
counts[maxCount].sort()
if len(counts[maxCount])==1:
    print(counts[maxCount][0])
else:
    print(counts[maxCount][1])

#차이
print(max(arr)-min(arr))
