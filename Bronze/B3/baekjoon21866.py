List= [100,100,200,200,300,300,400,400,500]
score = list(map(int,input().split()))
answer = "none"
if(sum(score)>=100):
    answer="draw"
for i in range(len(List)):
    if(score[i]>List[i]):
        answer="hacker"
        break
print(answer)