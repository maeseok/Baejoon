N,K = map(int,input().split())
fK = K%10
f2K = (2*K)%10
List=[]
for i in range(1,N+1):
    fi = i%10
    if(fi !=fK and fi!=f2K):
        List.append(str(fi))
print(len(List))
print(' '.join(List))