n=int(input())
arr=list(map(int,input().split()))
max = max(arr)
for i in range(len(arr)):
    arr[i]=arr[i]/max*100
print("{:.2f}".format(sum(arr)/len(arr)))