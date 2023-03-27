import sys
input=sys.stdin.readline
answer=[]
for i in range(int(input())):
    answer.append(input().split())
answer.sort(key=lambda x:int(x[0]))
for i in answer:
   print(" ".join(i))