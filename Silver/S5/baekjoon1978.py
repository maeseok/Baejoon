N=int(input())
List= list(map(int,input().split()))
cnt=0
for i in List:
    cnt2=0
    for j in range(2,i+1):
        if(i!=1):
            if(i%j==0):
                cnt2+=1
    if(cnt2==1):
        cnt+=1
print(cnt)