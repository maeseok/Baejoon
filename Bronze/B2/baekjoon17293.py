N = int(input())
a=""
b=""
for i in range(N+1):
    if i==N-1:
        a="1 bottle"
        b="no more bottles"
        print(a+" of beer on the wall, "+a+" of beer.")
        print("Take one down and pass it around, "+b+" of beer on the wall.")
        print()
    elif i==N-2:
        a="2 bottles"
        b="1 bottle"
        print(a+" of beer on the wall, "+a+" of beer.")
        print("Take one down and pass it around, "+b+" of beer on the wall.")
        print()
    elif i ==N:
        a="No more bottles"
        if(N==1):
            b="1 bottle"
        else:
            b=str(N)+" bottles"
        c="no more bottles"
        print(a+" of beer on the wall, "+c+" of beer.")
        print("Go to the store and buy some more, "+b+" of beer on the wall.")
    else:
        a=str(N-i)+" bottles"
        b=str(N-i-1)+" bottles"
        print(a+" of beer on the wall, "+a+" of beer.")
        print("Take one down and pass it around, "+b+" of beer on the wall.")
        print()