import sys
input = sys.stdin.readline
s=int(input())
ans=set()
for i in range(s):
    x= input().split()
    if x[0]=="all":
        ans=set([str(i) for i in range(1,20+1)])
    else:
        ans = set()
    if(x[0]=="add"):
        ans.add(x[1])
    elif(x[0]=="check"):
        if(x[1] in ans):
            print(1)
        else:
            print(0)
    elif(x[0]=="remove"):
        if x[1] in ans:
            ans.discard(x[1])
    elif(x[0]=="toggle"):
        if(x[1] in ans):
            ans.discard(x[1])
        else:
            ans.add(x[1])