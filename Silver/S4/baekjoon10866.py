import sys
input = sys.stdin.readline
N = int(input())
A=[]
for i in range(N):
    a=list(input().split())
    if("push_front" in a):
        A.insert(0,a[1])
    elif("push_back" in a):
        A.append(a[1])
    elif("pop_front" in a):
        if(A):
            print(A[0])
            A.pop(0)
        else:
            print(-1)
    elif("pop_back" in a):
        if(A):
            print(A[-1])
            A.pop(len(A)-1)
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
    else:
        if(A):
            print(A[-1])
        else:
            print(-1)