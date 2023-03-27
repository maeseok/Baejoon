ans=1
for _ in range(3):
    ans*=int(input())
ans=list(str(ans))
List=[i for i in range(0,10)]
for i in range(len(List)):
    print(ans.count(str(List[i])))