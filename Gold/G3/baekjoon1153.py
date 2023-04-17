n=int(input())
tmp=[False,False]+([True]*(n-1))
prime=[]
for i in range(2,n+1):
    if tmp[i]:
        prime.append(i)
        for j in range(2*i,n+1,i):
            tmp[j]=False
size=len(prime)

ans=[]
def goldbach(num):
    for i in range(size):
        for j in range(size):
            sum=prime[i]+prime[j]
            if sum==num:
                ans.extend([prime[i],prime[j]])
                return
            elif sum>num:
                break
if n<8:
    print(-1)
else:
    if n%2==0:
        ans=[2,2]
        n-=4
        goldbach(n)
        print(*ans)
    else:
        ans=[2,3]
        n-=5
        goldbach(n)
        print(*ans)