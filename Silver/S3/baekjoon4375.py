while True:
    try:
        n = int(input())
    except:
        break
    x="1"
    while True:
        X = int(x)
        if(X%n==0):
            print(len(x))
            break
        else:
            x +="1"