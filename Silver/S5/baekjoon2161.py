from collections import deque
queue=deque([i+1 for i in range(int(input()))])
ans=[]
i=0
while len(queue)>1:
    if i%2==0:
        x=queue.popleft()
        ans.append(x)
    else:
        x=queue.popleft()
        queue.append(x)
    i+=1
ans.append(queue.pop())
print(*ans)