import sys
ans={}
cnt=0
for i in sys.stdin:
    if i=='\n':
        break
    a=i.rstrip()
    cnt+=1
    if a in ans:
        ans[a]+=1
    else:
        ans[a]=1    
ans=sorted(ans.items(),key=lambda x:x[0])
for i in ans:
    x=i[1]/cnt*100
    print('{} {:.4f}'.format(i[0],x))