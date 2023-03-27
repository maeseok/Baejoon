a=input()
b=input()
ans=[0]*1000
for i in range(len(a)):
    tmp=0
    for j in range(len(b)):
        if tmp<ans[j]:
            tmp=ans[j]
        elif a[i]==b[j]:
            ans[j]=tmp+1
print(max(ans))