n=int(input())
arr=[False,False]+[True]*(n-1)
tmp=[]
for i in range(2,n+1):
    if arr[i]:
        tmp.append(i)
        for j in range(2*i,n+1,i):
            arr[j]=False
ans=0
start=0
end=0
while end<=len(tmp):
    tmp_sum=sum(tmp[start:end])
    if tmp_sum ==n:
        ans+=1
        end+=1
    elif tmp_sum <n:
        end+=1
    else:
        start+=1
print(ans)