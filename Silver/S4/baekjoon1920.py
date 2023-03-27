import sys
N = int(sys.stdin.readline())
List = list(map(int,sys.stdin.readline().split()))
M = int(sys.stdin.readline())
List2 = list(map(int,sys.stdin.readline().split()))
List.sort()
for num in List2:
    first,last = 0,N-1
    isExist = False
    #이분탐색 시작
    while first<=last:
        mid = (first+last)//2
        if num ==List[mid]:
            isExist = True
            print(1)
            break
        elif(num>List[mid]):
            first = mid+1
        else:
            last = mid-1
    if not isExist:
        print(0)