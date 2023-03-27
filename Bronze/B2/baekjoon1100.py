import sys

cnt =0
for i in range(8):
    #반복 입력 시 부하방지 위해 sys.stdin.readline 사용 
    a= sys.stdin.readline()
    for j in range(len(a)):
        if(i%2==0):
            if(j%2==0):
                if(a[j]=="F"):
                    cnt+=1
        else:
            if(j%2!=0):
                if(a[j]=="F"):
                    cnt+=1  
print(cnt)


