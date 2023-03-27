n=int(input())
if(n<100):
    print(n)
else:
    cnt=99
    x=0
    y=0
    sum=n-100+1
    for i in range(100,n+1):
        for j in range(len(str(i))-1):
            i=str(i)
            x=int(i[j+1])-int(i[j])
            if(j!=0):
                if(y!=x):
                    sum-=1
                    break
            else:
                y=x
    print(sum+cnt)