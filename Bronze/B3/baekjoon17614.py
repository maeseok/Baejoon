N =int(input())
cnt=0
for i in range(0,N+1):
    i = str(i)
    for j in range(len(i)):
        if(i[j] ==  "3" or i[j]=="6" or i[j] == "9"):
            cnt+=1
print(cnt)