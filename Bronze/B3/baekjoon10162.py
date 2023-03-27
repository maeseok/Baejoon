T =int(input())
a = 300
b = 60
c = 10
if(T%10!=0):
    print(-1)
    quit()
else:
    A = T // a
    T = T % a
    B = T // b
    T = T % b
    C = T // c
print(A ,B ,C)