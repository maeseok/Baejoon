T =int(input())
for _ in range(T):
    input()
    a=0
    N = int(input())
    for i in range(N):
        X = int(input())
        a +=X
    if(a%N==0):
        print("YES")
    else:
        print("NO")
