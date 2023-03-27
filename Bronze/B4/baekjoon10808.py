from string import ascii_lowercase
List = list(ascii_lowercase)
S = input()
X = []
for i in range(len(List)):
    X.append(0)
    for j in range(len(S)):
        if(List[i]==S[j]):
            X[i] += 1
print(*X,end=" ")