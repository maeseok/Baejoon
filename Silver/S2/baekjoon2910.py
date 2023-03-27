n,c=map(int,input().split())
tmp=list(map(int,input().split()))
arr={}
for i in tmp:
    try:
        arr[i]+=1
    except:
        arr[i]=1
arr=sorted(arr.items(),key=lambda x:x[1],reverse=True)
for i in arr:
    for j in range(i[1]):
        print(i[0],end=" ")