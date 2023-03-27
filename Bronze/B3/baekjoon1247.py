import sys
x= []
for _ in range(3):
    S = 0
    N = int(sys.stdin.readline())
    for i in range(N):
        a = int(sys.stdin.readline())
        S +=a
    if(S==0):
        x.append("0")
    elif(S>0):
        x.append("+")
    else:
        x.append("-")
for j in range(len(x)):
    print(x[j])