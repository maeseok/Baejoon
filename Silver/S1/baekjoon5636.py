n=100000
tmp=[False,False]+([True]*(n-1))
for i in range(2,int(n**0.5)+1):
    if tmp[i]:
        for j in range(2*i,n+1,i):
            tmp[j]=False
    prime=[i for i in range(2,n+1) if tmp[i]]
while True:
    n=input()
    if n=="0":
        break
    ans=2
    for i in prime:
        if str(i) in n:
            ans=i
    print(ans)