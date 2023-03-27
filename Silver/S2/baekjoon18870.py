n=int(input())
arr=list(map(int,input().split()))
tmp =set(arr)
tmp=list(tmp)
tmp.sort()

answer=dict()
for i in range(len(tmp)):
    answer[tmp[i]]=i
for i in arr:
    print(answer[i],end=" ")