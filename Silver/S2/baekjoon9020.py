def sosu(n):
    if n==1:
        return False
    for i in range(2,int(n**0.5)+1):
        if(n%i==0):
            return False
    return True

#이 풀이과정이 시간 단축 (중간부터 시작하여 점차 멀어지는 과정) 
for _ in range(int(input())):
    num = int(input())
    a,b = num//2,num//2
    while a>0:
        if sosu(a) and sosu(b):
            print(a, b)
            break
        else:
            a-=1
            b+=1    