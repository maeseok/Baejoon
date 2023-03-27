#백트랙킹, 재귀함수 학습 필요
def dfs(depth,idx):
    if depth==6:
        print(*out)
        return
    for i in range(idx,k):
        out.append(s[i])
        dfs(depth+1,i+1)
        out.pop()    
import sys
input = sys.stdin.readline
while True:
    List=list(map(int,input().split()))
    k=List[0]
    s=List[1:]
    if(k==0):
        break
    else:
        out=[]
        dfs(0,0)
    print()
        