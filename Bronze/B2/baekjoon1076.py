color = ["black","brown","red","orange","yellow","green","blue","violet","grey","white"]
#리스트.index(값)는 리스트 안의 해당 값의 위치를 반환한다.
a = color.index(input())
b = color.index(input())
c = color.index(input())
d = int(str(a)+str(b))*(10**c)
print(d)
"""
d=""
e=""
f=0
list = ["black","brown","red","orange","yellow","green","blue","violet","grey","white"]
for i in range(len(list)):
    if(a==b or a==c or b==c):
        if(a==b==c):
            if(a==list[i]):
                d +=str(i)
                e += str(i)
                f =10**i
        elif(a==c):
            if(a==list[i]):
                d +=str(i)
                f =10**i
            elif(b==list[i]):
                e +=str(i)
        elif(b==c):
            if(a==list[i]):
                d +=str(i)
            elif(b==list[i]):
                e += str(i)
                f =10**i
        elif(a==b):
            if(a==list[i]):
                d +=str(i)
                e +=str(i)
            elif(c==list[i]):
                f =10**i
    else:
        if(a == list[i]):
            d +=str(i)
        elif(b == list[i]):
            e +=str(i)
        elif(c == list[i]):
            f = 10**i
g = d+e
print(int(g)*int(f))
"""