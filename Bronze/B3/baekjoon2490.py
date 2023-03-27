import sys
for _ in range(3):
    List = list(map(int,sys.stdin.readline().split()))
    a = List.count(0)
    b = List.count(1)
    if(a==1 and b==3):
        print("A")
    elif(a==2 and b==2):
        print("B")
    elif(a==3 and b==1):
        print("C")
    elif(a==4 and b==0):
        print("D")
    else:
        print("E")