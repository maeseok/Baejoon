import sys
input =sys.stdin.readline
def gcd(a,b):
    while b>0:
        a,b=b,a%b
    return str(a)[-9:]
n=int(input().rstrip())
a=1
b=1
for i in list(map(int,input().split())):
    a*=i
m=int(input().rstrip())
for j in list(map(int,input().split())):
    b*=j
print(gcd(a,b))