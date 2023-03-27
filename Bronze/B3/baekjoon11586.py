N = int(input())
List=[]
for _ in range(N):
    List.append(input())
X = int(input())
if(X==2):
    for i in range(len(List)):
        List[i] = List[i][::-1]
if(X==3):
    List.reverse()
for i in range(len(List)):
    if(X==1):
        print(List[i])
    elif(X==2):
        print(List[i])
    else:
        print(List[i])