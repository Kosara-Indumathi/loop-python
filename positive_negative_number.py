# Notice that first number is positive, and the second number is negative, then again a positive and then negative number and so on should be printed. Pattern looks similar to this Positive (+) Number, Negative (-) Number, Positive (+) Number, Negative (-) Number and so on.
# We can make any number negative by mutiplying it by -1.
i=1
while i<=10:
    if i%2!=0:
        print(i,end=",")
    if i%2==0:
        print(-i,end=",")
    i=i+1




