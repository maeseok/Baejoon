import sys
input = sys.stdin.readline
n=1003003
ans=[]
arr=[False, False]+([True]*(n-1))
for i in range(2,n+1):
    if arr[i]:
        ans.append(str(i))
    for j in range(i*2,n+1,i):
        arr[j]=False
x=int(input().rstrip())
for i in range(len(ans)):
    if(int(ans[i])>=x):
        rev=ans[i][::-1]
        if(ans[i]==rev):
            print(ans[i])
            quit()    