import math
n=int(input())
a=str(math.factorial(n))
for i in a[::-1]:
    if i=='0':
        continue
    else:
        print(i)
        break