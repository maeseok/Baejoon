import sys
input = sys.stdin.readline
arr=[]
for _ in range(int(input())):
    arr.append(list(map(int,input().split())))
arr.sort(key=lambda x:x[1])
tmp=0
for i in range(len(arr)-1,-1,-1):
    if tmp==0:
        tmp=arr[i][1]-arr[i][0]
    else:
        if tmp>arr[i][1]:
            tmp=arr[i][1]-arr[i][0]
        else:
            tmp=tmp-arr[i][0]
if tmp<0:
    print(-1)
else:
    print(tmp)