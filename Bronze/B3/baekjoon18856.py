N = int(input())
print(N)
List=[1,2]
a = 3
for _ in range(N-3):
    List.append(a)
    a+=1
List.append(53)
print(*List)