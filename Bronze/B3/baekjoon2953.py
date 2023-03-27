arr=[]
for i in range(5):
    a=list(map(int,input().split()))
    arr.append(sum(a))
print(arr.index(max(arr))+1 ,max(arr))