i=1
s=1
while i<=5:
    j=1
    while j<=i:
        if i%2==0:
            print(" ",end=" ")
        else:
            print(s,end=" ")
            s=s+1
        j=j+1
    print()
    i=i+1