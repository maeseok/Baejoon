n,k= map(int,input().split())
arr=[]
sosu=[False,False]+([True]*(n-1))
cnt=0
for i in range(2,n+1):
    for j in range(i,n+1,i):
        if(j not in arr):
            arr.append(j)
            cnt+=1
        if(cnt==k):
            print(j)
            quit()