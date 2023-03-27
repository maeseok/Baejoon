#이것도 포스팅 ㄱㅊ
import sys
T = int(input())
A =[1,3,6,10,15,21]
A1=[5000000,3000000,2000000,500000,300000,100000]
B =[1,3,7,15,31]
B1=[5120000,2560000,1280000,640000,320000]
for _ in range(T):
    C=0
    X=0
    Y=0
    a,b = map(int,sys.stdin.readline().split())
    if(a<=21 and a>0):
        for i in range(6):
            if(A[5-i]>=a):
                C =5-i
        X=A1[C]
    if(b<=31 and b>0):
        for j in range(5):
            if(B[4-j]>=b):
                C=4-j
        Y=B1[C]
    print(X+Y)