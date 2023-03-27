n=int(input())
result=0
for i in range(n//2,n):
    i =str(i)
    sum=0
    sum+=int(i)
    for j in range(len(i)):
        sum+=int(i[j])
    if(sum==n):
        if result==0:
            result=i
        else:
            result=min(result,i)
print(result)