x,y,w,h = list(map(int,input().split()))
#min함수를 이용해 제일 작은 값 출력
print(min([x,y,w-x,h-y]))

"""
a=list(map(int,input().split()))
b=[]
b.append(a[2]-a[0])
b.append(a[3]-a[1])
b.append(a[0])
b.append(a[1])
b.sort()
print(b[0])
"""