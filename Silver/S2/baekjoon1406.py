import sys
#커서를 기준으로 2개로 나눈 풀이
#append와 pop이 O(1) 시간 연산
st1 = list(sys.stdin.readline().rstrip())
st2 = []

for _ in range(int(sys.stdin.readline())):
    command = list(sys.stdin.readline().split())
    if(command[0] == 'L'):
        if st1:
            #제일 마지막 값 삭제 후 값 취득
            st2.append(st1.pop())
            print(st2)
    elif command[0] == 'D':
    	if st2:
            st1.append(st2.pop())
            print(st1)
    elif command[0] == 'B':
    	if st1:
            st1.pop()
            print(st1)
    else:
        st1.append(command[1])
        print(st1)
print(st2)       
st1.extend(reversed(st2))
print(''.join(st1))







'''틀림
import sys
input = sys.stdin.readline
a = list(input().rstrip())
cur = len(a)
for i in range(int(input())):
    A = list(input().split())
    if(A[0]=="P"):
        a.insert(cur,A[1])
        cur+=1
    elif(A[0]=="L"):
        if cur>0:
            cur-=1
    elif(A[0]=="D"):
        if(cur<len(a)):
            cur+=1
    else:
        if cur>0:
            a.remove(a[cur-1])
print(''.join(a))'''