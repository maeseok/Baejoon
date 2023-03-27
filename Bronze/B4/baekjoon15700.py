#이것도 포스팅 고려
a,b = map(int,input().split())
if(a==1 or b==1):
    print(a*b//2)
else:
    if a%2:
        print((a//2)*b+b//2)
    else:
        print((a//2)*b)