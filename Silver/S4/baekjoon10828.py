import sys
N=int(input())
stack=[]
for i in range(N):
    List=list(map(str,sys.stdin.readline().split()))
    if("push" in List):
        stack.append(int(List[1]))
    elif("top" in List):
        if(len(stack)==0):
            print(-1)
        else:
            print(stack[-1])
    elif("size" in List):
        print(len(stack))
    elif("empty" in List):
        if(len(stack)==0):
            print(1)
        else:
            print(0)
    elif("pop" in List):
        if(len(stack)==0):
            print(-1)
        else:
            print(stack[-1])
            stack.pop(-1)