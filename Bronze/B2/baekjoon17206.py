import sys
N =int(sys.stdin.readline().rstrip())
List = list(map(int,sys.stdin.readline().split()))
#메모이제이션을 활용하여 80000까지의 배수 합을 배출
memo = [0] * 80001
ans = 0
for i in range(80001):
    if(i%3==0 or i%7==0):
        ans += i
    memo[i] = ans
for elem in List:
    print(memo[elem])