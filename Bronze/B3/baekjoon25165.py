n, m = map(int, input().split())
a, d = map(int, input().split())
x, y = map(int, input().split())

result = "NO..."
if x == n and n % 2 != d:
    result = "YES!"
print(result)

'''
N,M = map(int,input().split())
a,b = map(int,input().split())
c,d = map(int,input().split())
answer = "YES!"
for i in range(2,N+1):
    x=i
    for j in range(1,M+1):
        if(b==0):
            if(i%2==0):
                y=j
                if(x==c and y==d):
                    answer = "NO..."
                if(x==N and y==M):
                    break
                continue
            else:
                y=M+1-j
                if(x==c and y==d):
                    answer = "NO..."
                if(x==N and y==M):
                    break
                continue
        else:
            if(i%2==0):
                y=M+1-j
                if(x==c and y==d):
                    answer = "NO..."
                if(x==N and y==M):
                    break
                continue
            else:
                y=j
                if(x==c and y==d):
                    answer = "NO..."
                if(x==N and y==M):
                    break
                continue
print(answer)
'''