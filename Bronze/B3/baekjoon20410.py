m,seed,x1,x2 = map(int,input().split())
a=0
c=0
for i in range(100+1):
    for j in range(100+1):
        if((i*seed+j)%m ==x1 and (i*x1+j)%m ==x2):
            a =i
            c =j
            print(a ,c)
            quit()