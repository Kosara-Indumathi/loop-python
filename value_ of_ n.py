# Take an integer input in a variable named n. Take user input as many times as the value of n.
# Finally, print the sum of all those numbers which you have taken as an input.
# Example: If the user has put n value as 6, then take input for 6 times.
# Number of inputs to be taken? 6
# Enter a number > 10
# Enter a number > 1
# Enter a number > 56
# Enter a number > 89
# Enter a number > 11
# Enter a number > 12
# Sum: 179



i=1
sum=0
while i<=6:
    n=int(input("enter the number"))
    i=i+1
    sum=sum+n
print(sum)

    
