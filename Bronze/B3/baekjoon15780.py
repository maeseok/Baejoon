import sys
N,K = map(int,input().split())
cnt=0
List= list(map(int,sys.stdin.readline().split()))
for i in List:
    if(i%2==0):
        cnt += i//2
    else:
        cnt += i//2+1
if(cnt>=N):
    print("YES")
else:
    print("NO")