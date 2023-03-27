import sys
input = sys.stdin.readline
n,l = map(int,input().split())
arr=list(map(int,input().split()))
arr.sort()
start=arr[0]-0.5
end=start+l
count=1
for i in range(0,len(arr)):
    if start<arr[i]<end:
        continue
    else:
        count +=1
        start = arr[i]-0.5
        end=start+l
print(count)