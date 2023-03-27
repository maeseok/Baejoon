from itertools import permutations
n=int(input())
List = list(permutations(['1','2','3','4','5','6','7','8','9'],3))

for _ in range(n):
    a,b,c=map(int,input().split())
    a=list(str(a))
    cnt=0
    for i in range(len(List)):
        strike=ball=0
        i-=cnt
        for j in range(3):
            if List[i][j]==a[j]:
                strike+=1
            elif a[j] in List[i]:
                ball+=1
        if strike!=b or ball!=c:
            List.remove(List[i])
            cnt+=1
print(len(List))
