import sys
N = int(input())
List =[]
for _ in range(N):
    a,b,c = map(int,sys.stdin.readline().split())
    if(a==b==c):
        List.append(10000+a*1000)
    elif(a==b or b==c or a==c):
        if(a==b or a==c):
            List.append(1000+a*100)
        else:
            List.append(1000+b*100)
    else:
        List.append(max(a,b,c)*100)
print(max(List))