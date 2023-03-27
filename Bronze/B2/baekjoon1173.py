#시간, 초기맥박, 최대맥박, 운동, 휴식
N,m,M,T,R = map(int,input().split())
cnt =0
time=0
k=m
while True:
    if(cnt == N):
        print(time)
        break
    elif(m+T>M):
        print(-1)
        break
    elif(k+T<=M):
        k = k+T
        cnt += 1
        time += 1
    else:
        k = k-R
        if(k<m):
            k=m
        time +=1