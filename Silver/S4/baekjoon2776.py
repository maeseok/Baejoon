import sys
input =sys.stdin.readline

def search(s,e,num1,num):
    while s<=e:
        mid=(s+e)//2
        if num1[mid]==num:
            return 1
        elif num1[mid]<num:
            s=mid+1
        else:
            e=mid-1
    return 0

n=int(input())

for _ in range(n):
    x=int(input())
    a=list(map(int,input().split()))
    a.sort()
    y=int(input())
    b=list(map(int,input().split()))
    for num in b:
        print(search(0,x-1,a,num))