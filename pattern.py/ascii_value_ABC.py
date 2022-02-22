i=0
while i<=5:
    j=0
    k=ord("A")
    while j<=i:
        print(chr(k+i-j),end="")
        j=j+1
        k=k+1
    print()
    i=i+1