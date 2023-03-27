import sys
input = sys.stdin.readline
for i in range(int(input())):
    N,M =map(int,input().split())
    List=list(map(int,input().split()))
    idx = list(range(len(List)))
    idx[M] = 'target'
    cnt=0
    while True:
        if(List[0]==max(List)):
            cnt +=1
            if idx[0]== 'target':
                print(cnt)
                break
            else:
                List.pop(0)
                idx.pop(0)
        else:
            List.append(List.pop(0))
            idx.append(idx.pop(0))
            
        