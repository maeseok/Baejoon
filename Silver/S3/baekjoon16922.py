from itertools import combinations_with_replacement
n=int(input())
ans=set()
arr=[1,5,10,50]
for combi in combinations_with_replacement(arr, n):
    print(combi)
    ans.add(sum(combi))
print(len(ans))