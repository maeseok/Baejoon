N =int(input())
a = int(input())
A = [0,1,0,1,0]
B = [1,0,1,0,1]
if(N>=6):
    print("Love is open door")
else:
    for i in range(1,N):
        if(a == 0):
            print(A[i])
        else:
            print(B[i])