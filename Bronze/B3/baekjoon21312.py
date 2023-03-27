a=1
List = list(map(int,input().split()))
for i in range(len(List)):
    if(List[i]%2!=0):
        List.append(List[i])

if(len(List)==3):
    a=List[0]*List[1]*List[2]
else:
    for j in range(3,len(List)):
        a *=List[j]
print(a)