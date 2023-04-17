def Euler(n):
    ans=n
    for i in range(2,round(n**0.5)+1):
        if n%i==0:
            while n%i==0:
                n//=i
            ans*=1-(1/i)
    if n>1:
        ans*=1-(1/n)
    return ans
n=int(input())
ans=Euler(n)
print(round(ans))