from collections import deque
import sys
input = sys.stdin.readline
for i in range(int(input())):
    try:
        p = input()
        n = int(input())
        x = input().rstrip()[1:-1].split(",")
        queue = deque(x)
        cnt=0
        if n==0:
            queue=[]
        for j in p:
            if(j=="R"):
                cnt+=1
            elif(j=="D"):
                if(len(queue)==0):
                    raise ValueError
                else:
                    if cnt%2==0:
                        queue.popleft()
                    else:
                        queue.pop()
        if cnt %2==0:
            print("["+",".join(queue)+"]")
        else:
            queue.reverse()
            print("["+",".join(queue)+"]") 
    except:
        print("error")