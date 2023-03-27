n,k = map(int,input().split())
nums = list(range(1,n+1))
index = k-1
answer=[]
while True:
    answer.append(nums[index])
    nums = nums[:index]+nums[index+1:]
    if not nums:
        break
    index=(index+k-1)%len(nums)
print('<'+', '.join(list(map(str,answer)))+'>')