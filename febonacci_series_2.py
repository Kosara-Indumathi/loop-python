# Write a python program  to sum the sequence:
# 1 + 1/1! + 1/2! + 1/3! + …… + 1/n!
num=int(input("enter the number"))
i=1
sum=0
fact=1
while i<=num:
    fact=fact*i
    sum=sum+i/fact
    i=i+1
print(sum)
    
