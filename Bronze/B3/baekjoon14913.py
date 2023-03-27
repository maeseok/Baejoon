a,d,k = map(int,input().split())
#틀림
y = (k-a)//d
z = (k-a)%d
if(y>=0 and z==0):
    print(y+1)
else:
    print("X")