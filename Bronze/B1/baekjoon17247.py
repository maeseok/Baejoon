n,m=map(int,input().split())
tmp=[]
for i in range(n):
    s=list(map(int,input().split()))
    for j in range(len(s)):
        if s[j]==1:
             tmp.append([i,j])
print(abs(tmp[1][0]-tmp[0][0])+abs(tmp[1][1]-tmp[0][1]))
