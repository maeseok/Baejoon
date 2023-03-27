import sys
input = sys.stdin.readline
while True:
    a=input().rstrip()
    if(a=="0"):
        break
    b=a[::-1]
    if(a==b):
        print("yes")
    else:
        print("no")