n,k = map(int,input().split())
ans=[]
con = []
for _ in range(n):
    a=list(map(int,input().split()))
    if(a[0]==k):
        con=a[1:]
    ans.append(a[1:])
ans.sort(key=lambda x:(x[0],x[1],x[2]),reverse=True)
for i in range(len(ans)):
    if(ans[i]==con):
        print(i+1)
        break