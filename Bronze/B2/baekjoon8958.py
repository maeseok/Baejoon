import sys
input = sys.stdin.readline
n = int(input())
cnt=0
for i in range(n):
    sum=0
    a=input()
    for j in a:
        if(j=="O"):
            cnt+=1
            sum+=cnt
        else:
            cnt=0
    print(sum)