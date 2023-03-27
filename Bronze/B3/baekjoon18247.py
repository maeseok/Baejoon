T = int(input())
for i in range(T):
    N,M = map(int,input().split())
    if(N>=12 and M>=4):
        print(11*M+4)
    else:
        print(-1)