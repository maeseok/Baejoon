x1,y1,x2,y2,x3,y3=map(int,input().split())

#3개의 점이 1개의 선분 위에 있으면 사각형 생성 불가
# ((y1-y2)/(x1-x2) == (y1-y3)/(x1-x3))
if ((x1-x2)*(y1-y3) == (x1-x3)*(y1-y2)):
    print(-1.0)
    quit()

a = ((x1-x2)**2+(y1-y2)**2)**0.5
b = ((x1-x3)**2+(y1-y3)**2)**0.5
c = ((x2-x3)**2+(y2-y3)**2)**0.5

tmp = [a+b,a+c,b+c]
res = max(tmp)-min(tmp)
print(res*2)