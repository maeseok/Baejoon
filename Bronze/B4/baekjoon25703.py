n = int(input())
a = "&ptr;"
print("int a;")
print("int *ptr = &a;")
for i in range(2,n+1):
    print("int "+"*"*i+"ptr"+str(i)+" = "+a)
    a="&ptr"+str(i)+";"