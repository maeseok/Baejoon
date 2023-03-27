N =int(input())
List=[]
for _ in range(N):
    List.append(int(input()))
if(List.count(1)>List.count(0)):
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")