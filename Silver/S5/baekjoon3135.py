a,b=map(int,input().split())
arr=[]
for _ in range(int(input())):
    arr.append(int(input()))
if a>b:
    ans=a-b
elif a<b:
    ans=b-a
else:
    print(0)
    quit()
for i in arr:
    ans=min(ans,abs(b-i)+1)
print(ans)