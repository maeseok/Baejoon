import sys
input = sys.stdin.readline
stack=[]
for _ in range(int(input())):
    a=int(input())
    if(a==0):
        stack.pop()
    else:
        stack.append(a)
print(sum(stack))