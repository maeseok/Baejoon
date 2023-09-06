import sys
input=sys.stdin.readline
n=int(input())
user={}
ans=0
for i in range(n):
    x=input().strip()
    if x=="ENTER":
        for key,value in user.items():
            if value==1:
                ans+=1
        user={}
    else:
        if x not in user:
            user[x]=1
for key,value in user.items():
    if value==1:
        ans+=1
print(ans)