# Write a program to print the following series till n terms.
# 2 , 22 , 222 , 2222 _ _ _ _ _ n terms
num=int(input("enter the number"))
i=1
temp="2"
while i<=num:
    print(temp,end=",")
    temp=temp+"2"
    i=i+1
