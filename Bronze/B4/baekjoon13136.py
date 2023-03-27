#틀림
import math
a,b,c = map(int,input().split())
if a%c:
    a1 = a//c+1
else:
    a1 = a//c
if b%c:
    b1 = b//c+1
else:
    b1 = b//c
print(a1*b1)