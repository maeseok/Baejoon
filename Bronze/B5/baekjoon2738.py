import sys

a = []
b = []
#입력할 크기 입력받음
n,m = map(int,input().split())

#앞 데이터를 입력받아 저장
for i in range(n):
    data = list(map(int,sys.stdin.readline().split()))
    a.append(data)

#뒷 데이터를 입력받아 저장
for i in range(n):
    data = list(map(int,sys.stdin.readline().split()))
    b.append(data)

for i in range(n):
    for j in range(m):
    	#값을 더해 출력, 구분할 때는 띄어쓰기를 사용
        print(a[i][j]+b[i][j],end=" ")
    #한 줄 출력 후 다음 행으로
    print()