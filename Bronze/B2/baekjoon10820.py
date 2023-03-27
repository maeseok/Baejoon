while True:
    try:
        a=0
        b=0
        c=0
        d=0
        X=input()
        for i in X:
            if(i.islower()):
                a+=1
            elif(i.isupper()):
                b+=1
            elif(i.isdigit()):
                c+=1
            elif(i.isspace()):
                d+=1
        print(a,b,c,d)  
    except:
        break