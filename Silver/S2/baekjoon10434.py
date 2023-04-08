import sys
input = sys.stdin.readline

def happy(n):
    arr=[]
    x=0
    while True:
        if n<10:
            a1=n
            x=int(a1**2)
        elif n<100:
            a2=int(n/10)
            a1=n%10
            x=int(a2**2+a1**2)
        elif n<1000:
            a3=int(n/100)
            a2=int((n%100)/10)
            a1=n%10
            x=int(a3**2+a2**2+a1**2)
        elif x<10000:
            a4=int(n/1000)
            a3=int((n%1000)/100)
            a2=int((n%100)/10)
            a1=n%10
            x=int(a4**2+a3**2+a2**2+a1**2)
        if x==1:
            return 1
        if x in arr:
            return 0
        arr.append(x)
        n=x
        
n=10000
tmp=[False,False]+([True]*(n-1))
for i in range(2,int(n**0.5)+1):
    for j in range(2*i,n+1,i):
        if tmp[j]:
            tmp[j]=False
for _ in range(int(input())):
    a,b=map(int,input().split())
    if tmp[b]:
        x=happy(b)
        if x==1:
            print(a ,b ,"YES")
        else:
            print(a ,b ,"NO")
    else:
        print(a ,b ,"NO")