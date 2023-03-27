s=input()
arr=[]
cnt=1
while True:
    for i in range(len(s)):
        arr.append(s[i:i+cnt])
    cnt+=1
    if(cnt>len(s)):
        break
print(len(set(arr)))