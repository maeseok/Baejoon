def sum_num(x):
    res=0
    for i in x:
        if i.isdigit():
            res+=int(i)
    return res
serial=[input() for _ in range(int(input()))]
serial.sort(key=lambda x:(len(x),sum_num(x),x))
for i in serial:
    print(i)