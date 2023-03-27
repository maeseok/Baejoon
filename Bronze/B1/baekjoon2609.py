a,b = map(int,input().split())
A = 0
for i in range(1,max(a,b)+1):
    if(a%i==0 and b%i==0):
        A = i
print(A)
print(A*(a//A)*(b//A))    