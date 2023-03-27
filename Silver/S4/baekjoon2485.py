#최대공약수 함수
def gcd_func(a,b):
    while b!=0:
        a,b = b, a%b
    return a
n= int(input())
List=[]
a=0
b=0
for i in range(n):
    x = int(input())
    if(a==0):
        a=x
    else:
        b=x
        List.append(b-a)
        a=b
#List의 중복을 제거한 리스트
List_set = list(set(List))
#초기값은 첫번째 값
gcd=List_set[0]
for i in range(1,len(List_set)):
    #구한 gcd와 그 다음 값을 계속 비교해서 최종 gcd를 구함
    gcd = gcd_func(gcd,List_set[i])
#가로수 개수
cnt=0
for k in List:
    #각각 간격을 최대공약수로 나누고 1을 빼주면 심을 가로수 개수
    cnt += k//gcd -1
#최종적으로 심을 가로수 개수
print(cnt)