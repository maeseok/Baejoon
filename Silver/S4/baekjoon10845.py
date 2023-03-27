import sys
input = sys.stdin.readline
N = int(input())
A=[]
for i in range(N):
    a = list(input().split())
    if("push" in a):
        A.append(a[1])
    elif("pop" in a):
        if(A):
            print(A[0])
            A.pop(0)
        else:
            print(-1)
    elif("size" in a):
        print(len(A))
    elif("empty" in a):
        if(A):
            print(0)
        else:
            print(1)
    elif("front" in a):
        if(A):
            print(A[0])
        else:
            print(-1)
    elif("back" in a):
        if(A):
            print(A[-1])
        else:
            print(-1)