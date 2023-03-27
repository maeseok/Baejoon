N = int(input())
for _ in range(N):
    a = input()
    List=[]
    for i in a:
        if(i=="("):
            List.append(i)
        elif(i==")"):
            if List:
                List.pop()
            else:
                print("NO")
                break
    else:
        if not List:
            print("YES")
        else:
            print("NO")