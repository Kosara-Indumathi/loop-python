i=1
while i<=5:
    j=1
    while j<=i:
        if j==j+1:
            print(" ",end="")
        else:
            print(i*i,end="")
        j=j+1
    print()
    i=i+1
        