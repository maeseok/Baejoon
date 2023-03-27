#틀림 + 이해함
stack=[]
answer=[]
cur = 1
for i in range(int(input())):
    num=int(input())
    while cur<=num:
        stack.append(cur)
        answer.append("+")
        cur+=1
    if(stack[-1]==num):
        stack.pop()
        answer.append("-")
    else:
        print("NO")
        quit()
for i in answer:
    print(i)    