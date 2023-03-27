n=int(input())
x=1
for i in range(2,n+1):
    x*=i
    while True:
        if str(x)[-1]=="0":
            x//=10
        else:
            break
    x%=10**30
print(str(x)[-5:])