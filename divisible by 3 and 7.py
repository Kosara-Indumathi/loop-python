# Make a program that should do the following thing from 1 to 100.
# Numbers that are divisible by 3, you have to print "Nav".
# Numbers that are divisible by 7 so that "Gurukul" is printed.
# Numbers that are divisible by both 3 and 7, print "NavGurukul" there.
# If the number does not come in the above three cases then print the number only.


num=int(input("enter the number"))
i=1
while i<=num:
    if i%3==0 and i%7==0:
        print("navgurukul")
    elif i%3==0:
        print("nav")
    elif i%7==0:
        print("gurukul")
    else:
        print(i)
    i=i+1
    
        
        