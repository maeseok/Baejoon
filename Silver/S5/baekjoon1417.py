n=int(input())
arr=[]
for _ in range(n):
    arr.append(int(input()))
cnt=0
m=arr[0]
arr=arr[1:]
arr.sort(reverse=True)
if n==1:
    print(0)
else:
    while arr[0]>=m:
        m+=1
        arr[0]-=1
        cnt+=1
        arr.sort(reverse=True)
    print(cnt)