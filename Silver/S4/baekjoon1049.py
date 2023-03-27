import sys
input = sys.stdin.readline
n,m=map(int,input().split())
arr=[]
arr2=[]
for i in range(m):
    a,b=map(int,input().split())
    arr.append(a)
    arr2.append(b)
arr.sort()
arr2.sort()
if(arr[0]>=arr2[0]*6):
    print(n*arr2[0])
else:
    x=n//6
    y=n%6
    if(arr[0]<arr2[0]*y):
        x=x+1
        print(x*arr[0])
    else:
        print(x*arr[0]+y*arr2[0])