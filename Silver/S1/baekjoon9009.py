import sys
input = sys.stdin.readline
p = [1,2]
for i in range(2, 46):
    p.append(p[i-2]+p[i-1]) 
for i in range(int(input())):
    x=int(input().rstrip())
    res=[]
    while(x):
        for k in range(46):
            if(p[k]<=x):
                t=p[k]
        x-=t
        res.append(t)
    res.sort()
    for b in range(len(res)):
        print(res[b],end=' ')
    print()       