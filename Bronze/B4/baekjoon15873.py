a = input()
if(len(a)==2):
    print(int(a[0])+int(a[1]))
elif(len(a)==3):
    if(a[1]=="0"):
        b = a[0]+a[1]
        print(int(b)+int(a[2]))
    if(a[2]=="0"):
        b = a[1]+a[2]
        print(int(a[0])+int(b))
elif(len(a)==4):
    b = a[0]+a[1]
    c = a[2]+a[3]
    print(int(b)+int(c))