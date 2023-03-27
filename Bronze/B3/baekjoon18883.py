N,M = map(int,input().split())
X =N*M
for i in range(1,X+1):
    if(i%M==0):
        print(i)
        continue
    print(i,end=" ")