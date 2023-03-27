N = int(input())
c=[]
for i in range(N):
    a = list(map(str,input()))
    if(i==0):
        b= a
        c= b
    else:
        for j in range(0,len(b)):
            if(a[j] == b[j]):
                pass
            else:
                c[j]="?"
#헷갈렸던 내용
#join으로 리스트 값을 한줄로 출력
print(''.join(c))