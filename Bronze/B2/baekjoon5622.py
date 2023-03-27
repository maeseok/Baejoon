s = input()
List=[["A","B","C"],["D","E","F"],["G","H","I"],["J","K","L"],
      ["M","N","O"],["P","Q","R","S"],["T","U","V"],["W","X","Y","Z"]]
x=0
for i in s:
    for j in range(len(List)):
        if(i in List[j]):
            x+=j+3
print(x)