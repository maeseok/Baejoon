#마이너스의 나눗셈 - 포스팅
import math
N,M,K = map(int,input().split())
Y = K-3
X = M+Y
if(X%N>0):
    print(X%N)
elif(X%N==0):
    print(N)
