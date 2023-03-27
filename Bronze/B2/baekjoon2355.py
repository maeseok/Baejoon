#틀림
a,b = map(int,input().split())
c = max(a,b)
d = min(a,b)
print((c-d+1)*(a+b)//2)