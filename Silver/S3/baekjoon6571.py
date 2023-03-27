a=[None]*480
a[0],a[1]=1,2
for i in range(2,480):
    a[i]=a[i-1]+a[i-2]
while True:
    cnt=0
    x,y=map(int,input().split())
    if(x==0 and y==0):
        break
    for i in range(len(a)):
        if(a[i]>=x):
            if(a[i]<=y):
                cnt+=1
            else:
                break
    print(cnt)