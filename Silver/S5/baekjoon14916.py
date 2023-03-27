n=int(input())
a=n//5
ans=0
for i in range(a,-1,-1):
    if (n-5*i)%2==0:
        ans=i+(n-5*i)//2
        break
if ans==0:
    print(-1)
    quit()
else:
    print(ans)