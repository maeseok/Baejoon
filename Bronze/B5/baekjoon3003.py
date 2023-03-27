List=[1,1,2,2,2,8]
content = list(map(int,input().split()))
answer=[]
for i in range(len(content)):
    answer.append(List[i]-content[i])
#*를 사용하여 리스트 압축을 해제하여 한 줄로 출력
print(*answer)
