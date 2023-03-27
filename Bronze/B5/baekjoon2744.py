content = input()
answer = ""
for i in range(len(content)):
    #chr = 아스키코드를 문자로 변경
    if (content[i] >=chr(97)):
        #ord = 문자를 아스키코드로 변경
        answer+=chr(ord(content[i])-32)
    elif(content[i]<=chr(90)):
        answer+=chr(ord(content[i])+32)
print(answer)


a = input().rstrip()
b = '' 

for x in a :
    if x.isupper() : ## 대문자 인지 , islower() 소문자 인지 판별
        b += x.lower()
    else :
        b += x.upper()
print(b)
