import sys
List = []
y = 1
big = 0
x1 = 1
y1 = 1

for _ in range(1,10):
    List = list(map(int,sys.stdin.readline().split()))
    if(big<=max(List)):
        big = max(List)
        x1 = List.index(max(List)) +1
        y1 = y
    y+=1
print(big)
print(y1 ,x1)