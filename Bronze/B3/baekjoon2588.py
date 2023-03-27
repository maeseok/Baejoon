a = input()
b = input()
for i in range(1,len(b)+1):
    print(int(a)*int(b[len(b)-i]))
print(int(a)*int(b))