import sys
input = sys.stdin.readline
n=int(input())
for _ in range(n):
    t,s=map(str,input().split())
    output = ""
    for i in s:
        output+=i*int(t)
    print(output)