arr=[]
arr2=[]
for i in range(3):
    x,y=map(str,input().split())
    arr.append(x)
    arr2.append(y)
a=0
b=0
for i in range(len(arr)):
    if(arr.count(arr[i])==1):
        x=arr[i]
    if(arr2.count(arr2[i])==1):
        y=arr2[i]
print(int(x) ,int(y))