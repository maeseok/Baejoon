import math
cnt=1
while True:
    a,b,c=map(int,input().split())
    if a==b==c==0:
        break
    print("Triangle #"+str(cnt))
    if c==-1:
        c=math.sqrt(a**2+b**2)
        print("c = {:.3f}".format(c))
    elif a==-1:
        if b>=c:
            print("Impossible.") 
        else:
            a=math.sqrt(c**2-b**2)
            print("a = {:.3f}".format(a))
    else:
        if a>=c:
            print("Impossible.") 
        else:
            b=math.sqrt(c**2-a**2)
            print("b = {:.3f}".format(b))
    cnt+=1
    print()