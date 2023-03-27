int(input())
List = list(map(int,input().split()))
a=[]
for i in List:
    if(i not in a):
        a.append(i)
a.sort()
print(*a)