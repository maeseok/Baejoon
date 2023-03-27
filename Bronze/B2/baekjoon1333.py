import math
N,L,D = map(int,input().split())
cnt=0
while True:
    cnt+=1
    A = L*cnt+5*(cnt-1)
    B = math.ceil(A/D)
    if(cnt>=N):
        print(math.ceil(A/D)*D)
        quit()
    elif(A<=D*B<A+5):
        print(D*B)
        quit()