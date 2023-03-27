s = input()
List=[]
for i in range(len(s)):
    List.append(s[0+i:len(s)])
List.sort()
for i in range(len(List)):
    print(List[i])