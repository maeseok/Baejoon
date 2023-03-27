#알파벳 소문자 리스트
from string import ascii_lowercase
List = list(ascii_lowercase)
word = input()
for i in range(len(List)):
    if(List[i] in word):
        print(word.index(List[i]),end=" ")
    else:
        print(-1,end=" ")