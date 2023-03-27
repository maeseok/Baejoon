from string import ascii_lowercase, ascii_uppercase
lower = list(ascii_lowercase)
upper = list(ascii_uppercase)
N=input()
chr=""
for i in N:
    if(i in lower):
        i = lower.index(i)
        i = lower[(i+13)%len(lower)]
        chr+=i
    elif(i in upper):
        i = upper.index(i)
        i = upper[(i+13)%len(upper)]
        chr+=i
    else:
        chr+=i
print(chr)