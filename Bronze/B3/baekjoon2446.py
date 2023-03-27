N = int(input())
nbsp = -1
for i in range(2*N-1):
    if(i<=N-1):
        nbsp+=1
        print(" "*nbsp+"*"*(2*N-1-2*nbsp))
    else:
        nbsp-=1
        print(" "*nbsp+"*"*((2*N-1)-2*nbsp))