import sys
input = sys.stdin.readline
for _ in range(int(input())):
    x=int(input())
    for i in range(2,x+1):
        cnt=0
        if(x%i==0):
            while x%i==0:
                x=x//i
                cnt+=1
            print(i, cnt)