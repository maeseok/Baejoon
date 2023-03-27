n = int(input())
List=[]
for i in range(1,n+1):
    if(n%i==0):
        List.append(i)
print(sum(List)*5-24)