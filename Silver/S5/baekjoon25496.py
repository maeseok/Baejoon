p,n=map(int,input().split())
tmp=list(map(int,input().split()))
tmp.sort()
cnt=0
for i in tmp:
    if p<200:
        p+=i
        cnt+=1
    else:
        break
print(cnt)