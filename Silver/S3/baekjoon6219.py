a,b,d=map(int,input().split())
x=[False,False]+([True]*(b-1))
for i in range(2,int(b**0.5)+1):
    for j in range(2*i,b+1,i):
        x[j]=False
cnt=0
for i in range(a,b+1):
    if str(d) in str(i):
        if x[i]:
            cnt+=1
print(cnt)