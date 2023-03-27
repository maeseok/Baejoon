n = int(input())
c = list(map(int, input().split()))
max = 0

for i in range(n):
    if(c[i] == max%3):
        max+=1

print(max)
'''
N = int(input())
cnt = 0
List = list(map(int,input().split()))
if(0 in List):
    List = List[List.index(0):]
    cnt +=1
else:
    print(0)
    quit()
for i in range(len(List)-1):
    a = List[i]
    if(a==0):
        if(List[i+1]==1):
            cnt+=1
    elif(a==1):
        if(List[i+1]==2):
            cnt+=1
    elif(a==2):
        if(List[i+1]==0):
            cnt+=1
print(cnt)
'''