#딕셔너리 틀림
for _ in range(int(input())):
    clothes={}
    n = int(input())
    for _ in range(n):
        a,b = input().split()
        if(clothes.get(b) ==None):
            clothes[b]=set()
        clothes[b].add(a)
    cnt=1
    for key in clothes.keys():
        cnt *= len(clothes[key])+1
    print(cnt-1)