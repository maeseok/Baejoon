import sys
input = sys.stdin.readline
T=int(input())
List=list(map(int,input().split()))
for i in range(1,len(List)):
    for j in range(1,List[i]+1):
        if(List[0]%j==0 and List[i]%j==0):
            a=List[0]//j
            b=List[i]//j
    print(str(a)+"/"+str(b))