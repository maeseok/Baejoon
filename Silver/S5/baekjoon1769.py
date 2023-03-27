n=input()
cnt=0
tmp=n
arr=[3,6,9]
while True:
    if(len(tmp)==1):
        print(cnt)
        if(int(tmp) in arr):
            print("YES")
            quit()
        else:
            print("NO")
            quit()
    ans=0
    for i in tmp:
        ans+=int(i)
    tmp=str(ans)
    cnt+=1