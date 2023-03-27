import sys
from collections import deque
input = sys.stdin.readline
queue= deque([])
for _ in range(int(input())):
    a= input().rstrip()
    if("push" in a):
        a,b = a.split()
        queue.append(int(b))
    elif("pop" in a):
        if(len(queue)==0):
            print(-1)
        else:
            print(queue.popleft())
    elif("size" in a):
        print(len(queue))
    elif("empty" in a):
        if(len(queue)==0):
            print(1)
        else:
            print(0)
    elif("front" in a):
        if(len(queue)==0):
            print(-1)
        else:
            print(queue[0])
    else:
        if(len(queue)==0):
            print(-1)
        else:
            print(queue[-1])