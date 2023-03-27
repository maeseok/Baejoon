n=int(input())
arr=[]
for i in range(n):
    arr.append(list(map(int,input().split())))
arr.sort(key = lambda x:(x[0],x[1]))
opt=-1
for i in range(n):
    if(arr[i][0]>=opt):
        opt=arr[i][0]+arr[i][1]
    else:
        opt+=arr[i][1]
print(opt)