ans=0
for _ in range(5):
    a=int(input())
    if(a<=40):
        a=40
    ans+=a
print(int(ans/5))