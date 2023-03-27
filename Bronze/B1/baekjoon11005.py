n,b = map(int,input().split())
List='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#진법 변환 외우기
answer=''
while n!=0:
    answer += str(List[n%b])
    n=n//b
print(answer[::-1])