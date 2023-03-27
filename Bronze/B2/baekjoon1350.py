import math
a = 0
N = int(input())
List = list(map(int,input().split()))
size = int(input())
for i in List:
    a += math.ceil(i/size)
print(a*size)