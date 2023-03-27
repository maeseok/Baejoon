n = int(input())
List=[]
for i in range(n):
    List.append(input())
for i in range(n):
    print(List[i][0]+List[i][-1])