N,M = map(int,input().split())
a,b = map(int,input().split())
c,d = map(int,input().split())
#첫 번째 조건 못 찾음
if min(a,b) == min(c,d) and max(a,b) == max(c,d):
    print("YES")
elif(min(N,M) ==1):
    print("NO")
elif((a+b)%2==(c+d)%2):
    print("YES")
else:
    print("NO")