a,b = map(int,input().split())
c = int(input())

b += c%60
c = c//60
if(b>=60):
    a+=1
    b-=60
a += c%24
if(a>=24):
    a-=24
print(a ,b)