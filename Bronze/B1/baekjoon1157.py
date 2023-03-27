from string import ascii_uppercase
List = list(ascii_uppercase)
arr = [0]*len(List)
s= list(input())
for i in range(len(s)):
    if(s[i].isupper()):
        arr[List.index(s[i])]+=1
    else:
        s[i]=chr(ord(s[i])-32)
        arr[List.index(s[i])]+=1
a=arr.index(max(arr))
arr2=list(arr)
arr2.pop(a)
b=arr2.index(max(arr2))
if(arr[a]==arr2[b]):
    print("?")
else:
    print(List[a])