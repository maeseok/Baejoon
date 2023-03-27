import sys
input = sys.stdin.readline
for i in range(int(input())):
    arr=list(map(int,input().split()))
    cnt=0
    x=arr[0]
    arr=arr[1:]
    avg = sum(arr)/x
    for i in arr:
        if(i>avg):
            cnt+=1
    print("{:.3f}%".format(cnt/x*100))