a=[]
for _ in range(3):
    a.append(list(map(int,input().split())))
def ccw():
    tmp = a[0][0]*a[1][1]+a[1][0]*a[2][1]+a[2][0]*a[0][1]
    tmp -= (a[0][1]*a[1][0]+a[1][1]*a[2][0]+a[2][1]*a[0][0])
    return tmp
if ccw()==0:
        print("WHERE IS MY CHICKEN?")
else:
    print("WINNER WINNER CHICKEN DINNER!")