num=[1,1]
n=int(input())
if n<2:
    print(num[n])
else:
    for _ in range(n-1):
        num.append(num[-1]+num[-2]+1)
    print(num[-1]%1000000007)