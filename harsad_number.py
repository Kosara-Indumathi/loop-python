num=int(input("enter the number"))
temp=num
sum=0
while temp>0:
    rem=temp%10
    sum=sum+rem
    temp=temp//10
if num%sum==0:
    print("harsad")
else:
    print("not a harsad")