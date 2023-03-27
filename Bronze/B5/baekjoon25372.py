import sys
n = int(input())
for i in range(n):
    a=sys.stdin.readline()
    if(6<=len(a)-1<=9):
        print("yes")
    else:
        print("no")