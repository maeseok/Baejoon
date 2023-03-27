N = input()
for i in range(0,len(N),10):
    #str은 범위 넘어도 오류 발생x
    #EX) 길이 35 출력 30~40 -> 그래도 출력됨
    print(N[i:i+10])