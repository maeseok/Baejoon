import sys
n = int(input())
x=-1
for i in range(n):
    a,b=map(int,sys.stdin.readline().split())
    if(a<=b):
        if(x!=-1):
            if(x>b):
                x = b
        else:
            x = b
print(x)