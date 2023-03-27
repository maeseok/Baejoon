E,S,M = map(int,input().split())
e,s,m = 1,1,1
cnt=1
while True:
    if(e>15):
        e=1
    elif(s>28):
        s=1
    elif(m>19):
        m=1
    elif(e==E and s==S and m==M):
        print(cnt)
        quit()
    else:
        e+=1
        s+=1
        m+=1
        cnt+=1