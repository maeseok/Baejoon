n=int(input())
for i in range(1,n):
    print("*"*i+" "*2*(n-i)+"*"*i)
for i in range(0,n):
    print("*"*(n-i)+" "*i*2+"*"*(n-i))