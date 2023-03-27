import sys
input = sys.stdin.readline
dict = {"Y":2,"F":3,"O":4}
a,b=map(str,input().split())
ans=set([])
y = dict[b]-1
for i in range(int(a)):
    ans.add(input().rstrip())
print(len(ans)//y)