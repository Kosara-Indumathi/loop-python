# Write a program to find the sum of following series
# 1 + 8 + 27 …………n terms
num=int(input("enter the number"))
i=1
sum=0
while i<=num:
    sum=sum+i**3
    i=i+1
print(sum)