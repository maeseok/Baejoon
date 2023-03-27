List =[i for i in range(1,31)]
for i in range(28):
    a = int(input())
    List.remove(a)
print(min(List))
print(max(List))