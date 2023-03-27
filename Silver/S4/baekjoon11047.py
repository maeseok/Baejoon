import sys
input = sys.stdin.readline
N,K=map(int,input().split())
List=[]
cnt=0
sum=0
for i in range(N):
    List.append(int(input()))
x=len(List)-1
for j in range(len(List)):
    if(List[i]>=K):
        x=i
        break
for k in range(x,-1,-1):
    cnt+=K//List[k]
    K=K%List[k]
    sum+=K//List[k]*List[k]
    if(sum==K):
        print(cnt)
        break