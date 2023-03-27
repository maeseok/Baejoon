import sys
input = sys.stdin.readline
while True:
    n=int(input())
    if n==0:
        break
    li=[int(input()) for _ in range(n)]
    for i in range(1,n):
        li[i] = max(li[i],li[i]+li[i-1])
    print(max(li))