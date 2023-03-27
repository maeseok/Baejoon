n=int(input())
x=[False,False]+([True]*(n-1))
for i in range(2,int(n**0.5)+1):
    for j in range(2*i,n+1,i):
        x[j]=False
for i in range(2,n+1):
    if x[i]:
        tmp=[]
        z=i
        while True:
            sum=0
            for j in str(z):
                sum+=int(j)**2
            z=sum
            if(z in tmp):
                break
            if(z==1):
                print(i)
                break
            tmp.append(z)