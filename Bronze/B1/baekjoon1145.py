#5개의 숫자를 리스트에 저장 후 정렬
a = list(map(int,input().split()))
a.sort()
#찾을값 =f
f=1
#카운팅 횟수
cnt=0
#brute force start
while True:
    cnt=0
    #f 값을 a 값으로 나눈 나머지가 0일 때 cnt +1
    for i in range(0,len(a)):
        if(f%a[i]==0):
            cnt+=1
            #3이면 for문 나감
            if(cnt==3):
                break
    #이후 f를 출력 후 while문 종료
    if(cnt==3):
        print(f)
        break
    f+=1