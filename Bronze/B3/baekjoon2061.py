#틀림
K,L = map(int,input().split())
for i in range(2,int(L)):
    if(int(K)%i==0):
        print("BAD", i)
        exit()
print("GOOD")