def permutation(tmp,k):
    result=[]
    if k>len(tmp):
        return result
    if k==1:
        for i in tmp:
            result.append(i)
    elif n>1:
        for i in range(len(tmp)):
            ans=[i for i in tmp]
            ans.remove(tmp[i])
            for j in permutation(ans,k-1):
                result.append(tmp[i]+j)
    return result
n=int(input())
k=int(input())
tmp=[input() for _ in range(n)]
tmp.sort()
res=set(permutation(tmp,k))
print(len(res))