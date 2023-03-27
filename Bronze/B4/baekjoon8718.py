a,b = map(int,input().split())

A = 7*b
B = 7*b/2
C = 7*b/4
if(A<=a):
    print(int(A*1000))
elif(B<=a):
    print(int(B*1000))
elif(C<=a):
    print(int(C*1000))
else:
    print(0)
