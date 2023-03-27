import sys
input = sys.stdin.readline
arr=[]
for _ in range(int(input())):
    arr=[list(map(int,input().split())) for _ in range(4)]
    ans=[]
    for i in range(3):
        for j in range(i+1,4):
            ans.append((arr[i][0]-arr[j][0])**2+(arr[i][1]-arr[j][1])**2)
    ans.sort()
    if ans[0]==ans[1] and ans[0]==ans[2] and ans[0]==ans[3] and ans[4]==ans[5]:
        print(1)
    else:
        print(0)