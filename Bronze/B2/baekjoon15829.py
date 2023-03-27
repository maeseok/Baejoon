from string import ascii_lowercase
A = list(ascii_lowercase)
B = []
C = 0
for i in range(1,27):
    B.append(i)
L =int(input())
X = input()
for i in range(L):
    a = A.index(X[i])
    C += B[a]*31**i
print(C%1234567891)