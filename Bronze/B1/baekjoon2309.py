import sys
List=[]
x=[]
for i in range(9):
    List.append(int(sys.stdin.readline()))
for j in range(len(List)):
    for k in range(j+1,len(List)):
        x=list(List)
        x.remove(List[j])
        x.remove(List[k])
        if(sum(x)==100):
            List=x
            List.sort()
            for u in range(len(List)):
                print(List[u])
            quit()