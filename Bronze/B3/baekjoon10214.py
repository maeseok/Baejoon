import sys
T = int(input())
for _ in range(T):
    Y=0
    K=0
    for i in range(9):
        y,k = map(int,sys.stdin.readline().split())
        Y += y
        K += k
    if(Y>K):
        print("Yonsei")
    elif(Y==K):
        print("Draw")
    else:
        print("Korea")