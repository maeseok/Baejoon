import sys
N,M = map(int,input().split())
a = list(map(int,sys.stdin.readline().split()))
cnt = 0
for i in range(N-1):
    sum = 0
    b = list(map(int,sys.stdin.readline().split()))
    for j in range(M):
        sum += abs(a[j]-b[j])
    if(sum>2000):
        cnt +=1
N = N-1
if(cnt>=(N/2)):
    print("YES")
else:
    print("NO")