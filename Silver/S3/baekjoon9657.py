n=int(input())
arr=[0,"SK","CY","SK","SK"]+[0]*1000
stones=[1,3,4]
for i in range(5,n+1):
    for s in stones:
        if arr[i-s]=="CY":
            arr[i]="SK"
            break
        arr[i]="CY"
print(arr[n])