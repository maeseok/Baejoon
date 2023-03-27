n,w,h=map(int,input().split())
for _ in range(n):
    x=int(input())
    if w**2+h**2>=x**2:
        print("DA")
    else:
        print("NE")