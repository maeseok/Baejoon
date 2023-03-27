N,B = input().split()
N = ''.join(reversed(N))
B = int(B)
number = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
result = 0 
#진법 변환 외우기
for x in range(len(N)-1,-1,-1):
    sum = number.index(N[x])*(B**x)
    result += sum
print(result)