n = int(input())
a=list(map(int,input().split()))
a.sort()
a_min = a[0]
a_max = a[len(a)-1]
print(a_min*a_max)

#오답 내용
#1과 자기자신을 제외한 모든 약수가 주어졌기 때문에
#가장 작은 값과 큰 값을 곱하면 본질의 숫자가 나온다.




"""
b=[]
for i in range(0,n):
    b.append(a[i])
print(b)
c=b
for j in range(0,len(b)):
    for k in range(0,len(b)):
        if(b[j] % b[k] ==0):
            c[j] = c[j]/c[k]
"""