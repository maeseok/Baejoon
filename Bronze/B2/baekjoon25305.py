n,k=map(int,input().split())
List=list(map(int,input().split()))
List.sort(reverse=True)
print(List[k-1])