n=997
sosu=[]
arr=[False,False]+([True]*(n-1))
for i in range(2,n+1):
    if arr[i]:
       sosu.append(i)
    for j in range(i*2,n,i):
        arr[j]=False
def ans(x,sosu):
    for i in sosu:
        for j in sosu:
            for k in sosu:
                if i+j+k==x:
                    print(i,j,k)
                    return
for _ in range(int(input())):
    x=int(input())
    ans(x,sosu)