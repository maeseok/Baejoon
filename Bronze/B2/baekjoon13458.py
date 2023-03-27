import math
N=int(input())
List=list(map(int,input().split()))
B,C=map(int,input().split())
X=N
for i in List:
    i=i-B
    if(i<=0):
        pass
    else:
        X +=math.ceil(i/C)
print(X)