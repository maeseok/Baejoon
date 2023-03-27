List = list(map(int,input().split()))
x,y,z = map(int,input().split())
a = 0
for i in range(4):
    if(List[i]==x):
        a = i+1
print(a)
