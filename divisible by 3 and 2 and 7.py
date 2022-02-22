
num=int(input("enter the number"))
i=1
while i<=num:
    if i%3==0 and i%7==0:
        print(i,"milk")
    elif i%2==0:
        print(i,"curd")
    elif i%7==0:
        print(i,"kheer")
    else:
        print(i,"nothing")
    i=i+1
    
