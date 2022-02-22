#Write a program to find the sum of all even numbers that falls between two numbers (exclusive both numbers) entered from the user using while loop.
num1=int(input("enter the number"))
num2=int(input("enter the number"))  
if num1>num2:
   while num1>=num2:
    num2%2==0
    print(num2)
    num2=num2+2
else:
    while num2>=num1:
      num1%2==0
      print(num1)
      num1=num1+2

