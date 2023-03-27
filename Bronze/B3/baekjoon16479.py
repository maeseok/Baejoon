k=int(input())
d1,d2=map(int,input().split())
x,y=max(d1,d2),min(d1,d2)
print(k**2-((x-y)/2)**2)