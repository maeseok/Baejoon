import sys
N =int(input())
a=0
for _ in range(N):
    a += int(sys.stdin.readline())
print(a-(N-1))