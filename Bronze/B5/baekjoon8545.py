#처음부터 끝까지 역순으로 
print(input()[::-1])

import sys
line=sys.stdin.readline().strip()
reversed_line=""
for a in range(len(line)):
	reversed_line=str(line[a])+reversed_line
print(reversed_line)