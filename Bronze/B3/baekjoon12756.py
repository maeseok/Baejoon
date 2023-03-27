a,a1 = map(int,input().split())
b,b1 = map(int,input().split())
while True:
    a1 -=b
    b1 -=a
    if(a1<=0 or b1<=0):
        if(a1<=0 and b1<=0):
            print("DRAW")
            break
        elif(a1<=0):
            print("PLAYER B")
            break
        else:
            print("PLAYER A")
            break