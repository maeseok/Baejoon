#틀림
n= int(input())
arr = [[0]*101 for _ in range(101)]
for _ in range(n):
    x,y = map(int,input().split())
    for i in range(x,x+10):
        for j in range(y,y+10):
            arr[i][j]=1
answer=0
for i in arr:
    answer += i.count(1)
print(answer)