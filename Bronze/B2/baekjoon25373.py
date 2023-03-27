#완전 틀림
import math
N = int(input())
x=0
if(N>=28):
    print((N-1)//7+4)
    quit()
else:
    for i in range(1,8):
        if(N*2<=(i*i+i)):
            x =i
            break
print(x)