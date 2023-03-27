a=list(map(str,input()))
tmp={"H":1,"C":12,"O":16}
ans=[]
for i in a:
    if i=="(":
        ans.append(i)
    elif i==")":
        check=0
        while True:
            tar=ans.pop()
            if tar=="(":
                break
            check+=tar
        ans.append(check)
    elif i in tmp:
        ans.append(tmp[i])
    else:
        ans[-1]*=int(i)
print(sum(ans))