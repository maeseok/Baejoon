import sys
n,x,k = map(int,input().split())
X = x
for _ in range(k):
    a,b =map(int,sys.stdin.readline().split())
    if(a==X):
        X=b
    elif(b==X):
        X=a
print(X)