import sys
input = sys.stdin.readline
n=int(input())
ans={}
for _ in range(n):
    a=input().rstrip()
    if(a not in ans):
        ans[a]=1
    else:
        ans[a]+=1
max_ans = max(ans.values())
book=[]
for ans,num in ans.items():
    if num == max_ans:
        book.append(ans)
print(sorted(book)[0])