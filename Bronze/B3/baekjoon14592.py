import sys
N =int(input())
A =[]
B =[]
C =[]
for i in range(N):
    a,b,c= map(int,sys.stdin.readline().split())
    A.append(a)
    B.append(b)
    C.append(c)
if(A.count(max(A))==1):
    print(A.index(max(A))+1)
elif(B.count(min(B))==1):
    print(B.index(min(B))+1)
else:
    print(C.index(min(C))+1)