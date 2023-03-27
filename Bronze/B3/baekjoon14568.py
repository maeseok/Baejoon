N = int(input())
cnt=0
for i in range(1,N):
    if(i%2!=1):
        for j in range(1,N):
            for k in range(1,N):
                if(k>=j+2 and i+j+k==N):
                    cnt+=1
print(cnt)