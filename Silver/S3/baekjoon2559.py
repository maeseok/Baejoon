import sys
input = sys.stdin.readline
n,k = map(int,input().split())
arr=list(map(int,input().split()))

#시간 복잡도 줄이기
ans=[]
ans.append(sum(arr[:k]))

for i in range(n-k):
    ans.append(ans[i]-arr[i]+arr[k+i])
print(max(ans))