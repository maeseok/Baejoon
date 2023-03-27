p,q= map(int,input().split())
List=[]
for i in range(1,p+1):
    if(p%i==0):
        List.append(i)
try:
    print(List[q-1])
except:
    print(0)