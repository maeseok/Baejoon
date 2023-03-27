import sys
input = sys.stdin.readline
def factorial(n):
    ans=1
    for i in range(2,n+1):
        ans*=i
    return ans
T=int(input())
for _ in range(T):
    a,b=map(int,input().split())
    print(factorial(b)//factorial(a)//factorial(b-a))