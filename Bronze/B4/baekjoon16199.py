a,b,c = map(int,input().split())
a1,b1,c1 = map(int,input().split())

if(a1>a):
    if(b1>b):
        print(a1-a)
    elif(b1==b):
        if(c1>=c):
            print(a1-a)
        else:
            print(a1-a-1)
    else:
        print(a1-a-1)
else:
    print(0)
print(a1-a+1)
print(a1-a)