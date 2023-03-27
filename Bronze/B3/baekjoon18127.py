A,B = map(int,input().split())
a=1
b=1
for i in range(B):
    a += A-2
    b += a
print(b)
#3 -  2 3 4 5 6 1씩 증가
#4 -  3 5 7 9 11 2씩 증가
#5 -  4 7        3씩 증가