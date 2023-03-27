def d(n):
    n=int(n)
    for i in str(n):
        n+=int(i)
    return n
arr=[0]*10001
cnt=0
while True:
    cnt+=1
    n= d(str(cnt))
    if(n>=10001):
        break
    arr[d(cnt)]=1
    
for i in range(1,len(arr)-7):
    if(arr[i]==0):
        print(i)