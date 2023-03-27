#모름
d = int(input())
tmp = ''
while d:
    tmp = str(d % 9) + tmp
    d = d // 9
print(int(tmp))