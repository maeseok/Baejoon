a=[None]*10001
a[1],a[2]=1,1
tmp=[]
for i in range(1,int(input())+1):
    tmp.append(list(map(int,input().split())))
for j in range(3,max(tmp)[0]+1):
    a[j]=a[j-1]+a[j-2]
for i in range(len(tmp)):
    print("Case #"+str(i+1)+": "+str(a[tmp[i][0]]%tmp[i][1]))