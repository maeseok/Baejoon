b1,b2 = map(int,input().split())
d1,d2 = map(int,input().split())
j1,j2 = map(int,input().split())
B=max(abs(j1-b1),abs(j2-b2))
D = abs(j1-d1)+abs(j2-d2)
if(B>D):
    print("daisy")
elif(B<D):
    print("bessie")
else:
    print("tie")