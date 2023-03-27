n,s=map(int,input().split())
arr=list(map(int,input().split()))
if(len(arr)==1):
    print(abs(arr[0]-s))
    quit()

for i in range(len(arr)):
    if(arr[i]<s):
        arr[i]=s-arr[i]
    else:
        arr[i]=arr[i]-s

#유클리드 호제법
def gcd(a,b):
    while b>0:
        a,b=b,a%b
    return a

for i in range(len(arr)-1):
    x = gcd(arr[i],arr[i+1])
    arr[i+1]=x
print(arr[-1])