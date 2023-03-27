import sys
input = sys.stdin.readline
n=int(input())
tmp=[]
for i in range(1,n+1):
    x,y,v=map(int,input().split())
    d = (x**2+y**2)**0.5
    tmp.append((d/v,i))
tmp.sort(key=lambda x:(x[0],x[1]))
for i in range(n):
    print(tmp[i][1])