#틀림
a,b = map(int,input().split())
c,d = map(int,input().split())
N = int(input())
cnt = 0
while True:
    if a%10==N or a//10==N or b%10==N or b//10==N:
        cnt +=1
    if(a==c and b==d):
        break
    b+=1
    if(b==60):
        b=0
        a+=1
print(cnt)