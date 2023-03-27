n,m = map(int,input().split())
arr = [[False for _ in range(n)] for _ in range(n)]
for i in range(m):
    a,b = map(int,input().split())
    arr[a-1][b-1]= True
    arr[b-1][a-1]= True
res = 0

for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if not arr[i][j] and not arr[i][k] and not arr[j][k]:
                res+=1
print(res) 