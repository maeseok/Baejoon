n=int(input())
tmp=[]
for _ in range(n):
    tmp.append(list(map(int,input().split())))
tmp.sort(key=lambda x:x[0])
mid_x = tmp[n//2][0]
tmp.sort(key=lambda x:x[1])
mid_y = tmp[n//2][1]

ans=0
for i in tmp:
    ans+=abs(mid_x-i[0])+abs(mid_y-i[1])
print(ans)