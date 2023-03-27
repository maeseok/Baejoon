import sys
input = sys.stdin.readline
n=int(input())
d=[0]*(n+1)
for i in range(2,n+1):
    #결국 점화식 풀기위해서는 다 나열해봐야됨 -> 노트 필기
    d[i] = d[i-1]+1
    if i%3==0:
        d[i]=min(d[i],d[i//3]+1)
    if i%2==0:
        d[i]=min(d[i],d[i//2]+1)
print(d[n])