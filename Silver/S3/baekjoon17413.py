#틀림
List =list(input().rstrip())
i=0
start=0

while i<len(List):
    if(List[i]=="<"):
        i+=1
        while List[i]!=">":
            i+=1
        i+=1
    elif(List[i].isalnum()):
        start=i
        while i<len(List) and List[i].isalnum():
            i+=1
        tmp = List[start:i]
        tmp.reverse()
        List[start:i]=tmp
    else:
        i+=1
print("".join(List))