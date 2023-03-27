#dp로 풀어야함 처음부터 끝까지 최댓값을 올려가며
n=int(input())
p = list(map(int,input().split()))
p.insert(0,0)
dp=[0 for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(1,i+1):
        #점화식이 관건
        dp[i]= max(dp[i], p[j]+dp[i-j])
print(dp[n])


'''
N=int(input())
List= list(map(int,input().split()))
arr=[]
for i in range(len(List)):
    arr.append(List[i]/(i+1))
def sol(arr,N):
    N2=N
    cnt=0
    sum=0
    while True:
        x=arr.index(max(arr))
        if(N2<x+1):
            arr.pop(x)
        else:
            sum+= N2//(x+1)*max(arr)*(x+1)
            cnt+= N2//(x+1)*(x+1)
            if(cnt==N):
                print(int(sum))
                quit()
            N2 = N2%(x+1)
sol(arr,N)
'''