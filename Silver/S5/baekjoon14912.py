n,m=map(int,input().split())
arr=[i for i in range(1,n+1)]
cnt=0
for i in arr:
    i=str(i)
    for j in i:
        if(j==str(m)):
            cnt+=1
print(cnt)