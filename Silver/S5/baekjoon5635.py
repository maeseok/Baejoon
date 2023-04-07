tmp=[]
for _ in range(int(input())):
    n,d,m,y=input().split()
    tmp.append([n,int(d),int(m),int(y)])
tmp.sort(key=lambda x:(x[3],x[2],x[1])) 
print(tmp[-1][0])
print(tmp[0][0])