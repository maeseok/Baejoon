#소수가 저장되는 리스트
prime = []
n=1000000
#에라토스테네스의 체
arr = [False, False] + ([True] * (n - 1))
for i in range(2, n+1):
    if arr[i]:
        prime.append(i)
    for j in range(i * 2, n, i):
        arr[j] = False
        
ans=[]
for i in range(int(input())):
    a = int(input())
    cnt=0
    for i in range(len(arr)):
        if prime[i]>a-prime[i]:
            break
        if arr[a-prime[i]]:
            cnt+=1
    ans.append(cnt)
print(*ans, sep='\n')