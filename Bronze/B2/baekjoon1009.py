#처음부터 끝까지 오답
n = int(input())

for i in range(0,n): 
    a,b = map(int,input().split())
    a = a % 10
    #1. 0인 경우
    if(a==0):
        print(10)
    #2. 1가지 경우만 나오는 경우
    elif(a==1 or a==5 or a==6):
        print(a)
    #3. 2가지 경우가 나오는 경우
    elif(a==4 or a==9):
        b= b % 2
        if(b==1):
            print(a)
        else:
            print((a*a)%10)
    #4. 4가지 경우가 나오는 경우
    else:
        b= b%4
        if(b==0):
            print(a**4%10)
        else:
            print(a**b%10)




