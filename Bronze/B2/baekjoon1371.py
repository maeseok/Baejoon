import sys
a = sys.stdin.read()
res = [0]*26

for i in a:
    if i.islower():
        res[ord(i)-97] += 1
for i in range(len(res)):
	# max 값은 int 이므로 최댓값과 같은 값을 가진 위치의 문자 출력
    if res[i] == max(res):
        print(chr(i+97), end='')