import math
a,b = map(int,input().split())
X=math.ceil(a/4)-math.ceil(b/4)
Y=(a%4)
if(Y==0):
    Y+=4
Z=(b%4)
if(Z==0):
    Z+=4
print(abs(X)+abs(Y-Z))