#식 모름
T=int(input())
for _ in range(T):
    x1,y1,x2,y2 = list(map(int,input().split()))
    n=int(input())
    count=0
    for _ in range(n):
        #행성 중심과의 거리가 모두 행성의 반지름보다 작은 경우만 x
        cx,cy,cr = map(int,input().split())
        dis1 = (x1-cx)**2+(y1-cy)**2
        dis2 = (x2-cx)**2+(y2-cy)**2
        pow_cr = cr**2
        
        if pow_cr> dis1 and pow_cr>dis2:
            pass
        elif pow_cr >dis1:
            count+=1
        elif pow_cr >dis2:
            count+=1
    print(count)