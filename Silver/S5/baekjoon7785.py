import sys
input = sys.stdin.readline
tmp=dict()
for _ in range(int(input())):
    a,b=map(str,input().split())
    if b=="enter":
        tmp[a]=b
    if b=="leave":
        del tmp[a]
tmp=sorted(tmp.keys(),reverse=True)
for i in tmp:
    print(i)