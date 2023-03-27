List = list(map(int,input().split()))
List.remove(max(List))
List.remove(min(List))
print(*List)