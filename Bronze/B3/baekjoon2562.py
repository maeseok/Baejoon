import sys
List =[]
for i in range(9):
    List.append(int(input()))
X = max(List)
Y = List.index(X) +1
print(X)
print(Y)