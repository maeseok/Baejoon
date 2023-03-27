import sys

while True:
    n,m = map(int,sys.stdin.readline().split())
    if(n>m):
        print("Yes")
    #둘다 0 0입력 받을 시 프로그램 종료
    elif(n==0 and m==0):
        break
    else:
        print("No")