import sys
input = sys.stdin.readline
n=int(input())
tmp=[]

for _ in range(n):
    left=[]
    right=[]
    pwd=input().rstrip()
    for i in pwd:
        if i=="<":
            if left:
                right.append(left.pop())
        elif i==">":
            if right:
                left.append(right.pop())
        elif i=="-":
            if left:
                left.pop()
        else:
            left.append(i)
    print("".join(left)+"".join(reversed(right)))