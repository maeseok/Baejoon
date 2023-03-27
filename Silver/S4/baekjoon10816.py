#이분 탐색도 시간초과, 딕셔너리 형태 이용
int(input())
a = list(map(int,input().split()))
c= dict()
for i in a:
    if i in c:
        c[i]+=1
    else:
        c[i]=1
int(input())
b=list(map(int,input().split()))
for i in b:
    if i in c:
        print(c[i],end=" ")
    else:
        print(0,end=" ")