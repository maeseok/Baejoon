import sys
input = sys.stdin.readline
N=int(input())
List=list(map(int,input().split()))
List.sort()
M=int(input())
List2=list(map(int,input().split()))
List3 = [0]*len(List2)
for i in range(len(List2)):
    first=0
    last=N-1
    while first<=last:
        mid=(first+last)//2
        if(List2[i]==List[mid]):
            List3[i]+=1
            break
        elif(List2[i]>List[mid]):
            first=mid+1
        else:
            last=mid-1 
print(*List3)