from string import ascii_uppercase
import sys
T=int(input())
for _ in range(T):
    a=0
    List = list(ascii_uppercase)
    N =sys.stdin.readline()
    for i in range(len(N)):
        if(N[i] in List):
            List.remove(N[i])
    for j in range(len(List)):
        a += ord(List[j])
    print(a)