List = list(map(int,input().split()))


while True:
    for i in range(len(List)-1):
        if(List[i]>List[i+1]):
            x = List[i]
            List[i] = List[i+1]
            List[i+1] = x
    if(List[0]<List[1]<List[2]):
        break
print(*List)