# Make an algorithm that prints the first 100 numbers of the fibonacci series.
# Fibonacci series is shown here,
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
# In this series first_number is 0 andsecond_number is 1. After this, the next number will be the sum of the last two numbers.
# Like, third_number = first_number + second_number
# 1 = 0 + 1
# fourth_number = second_number + third_number
# 2 = 1 + 1

i=0
first=0
second=1
while i<=10:
    print(first,end=",")
    temp=first
    first=second
    second=second+temp
    i=i+1
