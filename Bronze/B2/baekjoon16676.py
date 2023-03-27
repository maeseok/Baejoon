#문제 제대로 이해 못해서 틀림
N = input()
s = '1'*len(N)
if(len(N)==1):
    print(1)
else:
    if(int(N)>=int(s)):
        print(len(N))
    else:
        print(len(N)-1)