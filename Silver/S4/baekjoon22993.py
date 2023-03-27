n=int(input())
arr=list(map(int,input().split()))
x=arr[0]
arr=arr[1:]
arr.sort()
for i in arr:
    if x>i:
        x+=i
    else:
        print("No")
        quit()
print("Yes")