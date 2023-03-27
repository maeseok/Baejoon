from collections import deque
N=int(input())
arr = list(i for i in range(1,N+1))
ans = deque(arr)
while True:
    if(len(ans)==1):
        print(*ans)
        break
    ans.popleft()
    x=ans.popleft()
    ans.append(x)