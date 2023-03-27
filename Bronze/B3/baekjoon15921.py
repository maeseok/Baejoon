N = int(input())
if(N==0):
    print("divide by zero")
    quit()
else:
    List = list(map(int,input().split()))
a=0
x=0
for i in range(len(List)):
    a += List[i]
    x += List[i]/N
print('{:.2f}'.format(a/N/x))
