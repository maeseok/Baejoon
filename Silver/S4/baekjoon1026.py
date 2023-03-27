int(input())
A = list(map(int,input().split()))
A.sort()
B=list(map(int,input().split()))
B.sort()
B.reverse()
sum=0
for i in range(len(A)):
    sum+=A[i]*B[i]
print(sum)