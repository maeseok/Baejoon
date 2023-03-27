#코드가 너무 긺
n = int(input())
X=0
Y=0
List = list(map(int,input().split()))
for i in range(len(List)):
    X += List[i]//30*10
    if(List[i]%30!=0):
        X += 10
    elif(List[i]%30==0 and List[i]>=30):
        X += 10
    Y += List[i]//60*15
    if(List[i]%60!=0):
        Y += 15
    elif(List[i]%60==0 and List[i]>=60):
        Y +=15
if(X>Y):
    print("M", Y)
elif(X==Y):
    print("Y M", X)
else:
    print("Y", X)