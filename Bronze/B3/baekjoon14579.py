A=1
B=0
a,b = map(int,input().split())
for i in range(1,a):
    B+=i
for j in range(a,b+1):
    B += j
    A *= B
print(A%14579)