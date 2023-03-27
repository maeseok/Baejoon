def factorial(n):
    ans=1
    for i in range(2,n+1):
        ans*=i
    return ans
x = str(factorial(int(input())))
cnt=0
for i in range(len(x)-1,-1,-1):
    if(x[i]!="0"):
        break
    else:
        cnt+=1
print(cnt)