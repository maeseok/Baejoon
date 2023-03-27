a,p=map(int,input().split())
tmp=[a]
x=a
while True:
    y=0
    for i in str(x):
        y+=int(i)**p
    x=y
    if x in tmp:
        z= tmp.index(x)
        tmp=tmp[:z]
        break
    else:
        tmp.append(x)
print(len(tmp))