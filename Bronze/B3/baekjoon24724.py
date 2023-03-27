import sys
i=1
for _ in range(int(sys.stdin.readline())):
    N = int(sys.stdin.readline())
    a,b = map(int,sys.stdin.readline().split())
    for _ in range(N):
        a,b = map(int,sys.stdin.readline().split())
    print("Material Management "+str(i))
    print("Classification ---- End!")
    i+=1