n = int(input())
List = list(map(int,input().split()))
Next = -1
battery = 0
y=1
for i in range(n):
    if(List[i]!=Next):
        battery+=2
        y=2
    else:
        battery += 2*y
        y *= 2
    Next=List[i]
    if(battery>=100):
        battery=0
        Next =-1
        y=1
print(battery)