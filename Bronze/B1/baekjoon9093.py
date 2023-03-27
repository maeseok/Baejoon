import sys
N = int(sys.stdin.readline())
for i in range(N):
    List = list(map(str,sys.stdin.readline().split()))
    List2=[]
    for j in List:
        a=""
        for k in j:
            a= k+a
        List2.append(a)
    print(*List2)
    
'''
import sys
N = int(sys.stdin.readline())

for i in range(N):
    word = list(sys.stdin.readline().split())
    for j in word:
        print(j[::-1],end=' ')'''