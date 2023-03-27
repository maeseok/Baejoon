n = int(input())
x = n%8
if(x==1):
    print(1)
elif(x==5):
    print(5)
elif(x==3 or x==7):
    print(3)
else:
    if(n%8==4 or n%8==6 ):
        print(4)
    elif(n%8==0 or n%8==2):
        print(2)