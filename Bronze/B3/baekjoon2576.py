import sys
List=[]
for i in range(7):
    a = int(input())
    if(a%2!=0):
        List.append(a)
if(List):
    print(sum(List))
    print(min(List))
else:
    print(-1)