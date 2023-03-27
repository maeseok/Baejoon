a,b=map(str,input().split())
a,b=int(a[::-1]),int(b[::-1])
ans=str(a+b)
ans=ans[::-1]
print(int(ans))