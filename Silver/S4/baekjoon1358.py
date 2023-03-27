import sys,math
input=sys.stdin.readline
w,h,x,y,p=map(int,input().split())
r=h/2
arr=[]
cnt=0
for _ in range(p):
    arr.append(list(map(int,input().split())))
for i in arr:
    if x<=i[0]<=x+w and y<=i[1]<=y+h:
        cnt+=1
    else:
        a = math.sqrt((i[0]-x)**2+(i[1]-(y+r))**2)
        b = math.sqrt((i[0]-(x+w))**2+(i[1]-(y+r))**2)
        if a<=r or b<=r:
            cnt+=1
        else:
            pass
print(cnt)