import sys
input =sys.stdin.readline
def sosu(n):
    if n==1:
        return False
    for i in range(2,int(n**0.5)+1):
        if(n%i==0):
            return False
    return True
arr=[]
#전체 범위의 소수를 구하여 부하 줄임
all = list(range(2,246912))
for i in all:
    if sosu(i):
        arr.append(i)

n=int(input())
while True:
    cnt=0
    if n==0:
        break
    #구한 소수가 범위에 있을 때 cnt추가 
    for i in arr:
        if n<i<=2*n:
            cnt+=1
    print(cnt)
    n=int(input())