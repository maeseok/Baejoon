x=int(input())
def sosu(n):
    if n==1:
        return False
    for i in range(2,int(n**0.5)+1):
        if(n%i==0):
            return False
    return True

def dfs(num):
    if len(str(num))==x:
        print(num)
    else:
        for i in range(10):
            temp=num*10+i
            if sosu(temp):
                dfs(temp)
dfs(2)  
dfs(3)
dfs(5)
dfs(7)