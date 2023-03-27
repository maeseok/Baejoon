import sys
from collections import deque
input = sys.stdin.readline

n=int(input())
buffer=deque([])
while True:
    a= int(input().rstrip())
    if(a==-1):
        break
    if(a==0):
        buffer.popleft()
    else:
        if(len(buffer)>=n):
            pass
        else:
            buffer.append(a)
if(len(buffer)==0):
    print("empty")
else:
    print(*buffer)