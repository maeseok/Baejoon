n,k=map(int,input().split())
arr=[i for i in range(1,n+1)]
ans=[]
a=0
while arr:
    a+=k-1
    if a>=len(arr):
        a %= len(arr)
    x=arr.pop(a)
    ans.append(str(x))
print("<"+", ".join(ans)+">")