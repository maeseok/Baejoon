n,m=map(int,input().split())
tmp,tmp2={},{}
for _ in range(n):
    team=input()
    mem=[]
    for i in range(int(input())):
        name=input()
        tmp[name]=team
        mem.append(name)
        mem.sort()
    tmp2[team]=mem
for _ in range(m):
    s=input()
    num=int(input())
    if num==1:
        print(tmp[s])
    else:
        print('\n'.join(tmp2[s]))