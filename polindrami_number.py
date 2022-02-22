n=int(input("enter the number"))
temp=n
sum=0
while temp>0:
    digit=temp%10
    sum=sum*10+digit
    temp=temp//10
if n==sum:
    print("polindrame")
else:
    print("not a polindrame")




