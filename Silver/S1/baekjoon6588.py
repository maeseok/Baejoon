#소수가 저장되는 리스트
n=1000000
#에라토스테네스의 체
arr = [False, False] + ([True] * (n - 1))
for i in range(2, 1001):
    if arr[i]:
        for j in range(i * 2, n, i):
            arr[j] = False
        
ans=[]
while True:
    a=int(input())
    if(a==0):
        break
    for i in range(3,n):
        if arr[i]:
            if arr[a-i]:
                print("%d = %d + %d"%(a,i,a-i))
                break