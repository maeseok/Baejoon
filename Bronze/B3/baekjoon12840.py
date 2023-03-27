#이것도 포스팅 ㄱㅊ
import sys
h,m,s = map(int,input().split())
q =int(input())
for i in range(q):
    try:
        T,c = map(int,sys.stdin.readline().split())
        if(T==1):
            s += c%60
            c = c//60
            if(s>=60):
                m +=1
                s -=60
            m += c%60
            c = c//60
            if(m>=60):
                h+=1
                m -=60
            h += c%24
            if(h>=24):
                h -=24
        elif(T==2):
            s -= c%60
            c= c//60
            if(s<0):
                m -=1
                s +=60
            m -= c%60
            c = c//60
            if(m<0):
                h -=1
                m +=60
            h -= c%24
            if(h<0):
                h +=24
    except:
        print(h ,m ,s)
#datetime 함수를 사용하여서 푼 문제
"""
from datetime import datetime, timedelta
import sys

input = sys.stdin.readline
h,m,s = list(map(int,input().split()))
t=datetime(2000,1,1,h,m,s)
for _ in range(int(input())):
    arr=list(map(int,input().split()))
    if arr[0]==1:
        t+=timedelta(seconds=arr[1])
    elif arr[0]==2:
        t-=timedelta(seconds=arr[1])
    else:
        print(t.hour,t.minute,t.second)"""