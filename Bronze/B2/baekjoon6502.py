i=1
while True:
    List=list(map(int,input().split()))
    if List[0]==0:
        break
    r,w,l=List
    x=(w/2)**2+(l/2)**2
    if r**2>=x:
        print("Pizza "+str(i)+" fits on the table.")
    else:
        print("Pizza "+str(i)+" does not fit on the table.")
    i+=1