import sys
n,m = map(int,input().split())
list=[]
b=""
for i in range(n):
    a= sys.stdin.readline().strip()
    for j in range(m):
        b = a[j]+b
    list.append(b)
    b=""
for i in range(len(list)):
    print(list[i])

