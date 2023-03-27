N = int(input())
cnt = 0
for i in range(1,N+1):
    a=0
    b=i
    for j in str(i):
        a += int(j)
    if(b%a==0):
        cnt +=1
print(cnt)