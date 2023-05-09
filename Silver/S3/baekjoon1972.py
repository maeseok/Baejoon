while(1):
    x=input().rstrip()
    if x=="*":
        break
    for d in range(1,len(x)-1):
        tmp=set()
        for i in range(len(x)-d):
            s=x[i]+x[i+d]
            if s in tmp:
                print(x+" is NOT surprising.")
                break
            else:
                tmp.add(s)
        else:
            continue
        break
    else:
        print(x+" is surprising.")