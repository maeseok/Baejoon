"""#for문 해설법
a = input()
b = int(input())
#맨 뒷자리를 00으로 변경
a = int(a[:-2] +'00')
#00부터 99까지 1씩 증가하며 나눠지는 수 찾기
for i in range(100):
    if((a+i) % b ==0):
        #0~9사이인경우 앞에 0붙여서 출력
        if(0<=i<=9):
            print('0'+str(i))
            break
        #2번 출력되지 않게 break
        else:
            print(i)
            break
"""
#while문 해설법
a = input()
b = int(input())
a= int(a[:-2]+"00")
while True:
    if a % b ==0:
        break
    a+=1
print(str(a)[-2:])







"""
c= a%b
d=[]
d = d.append(a)
print(d)
if(c==0):
    print(00)
else:
    d= d[-2:]
    print(d)
"""