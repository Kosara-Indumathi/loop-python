i=1
count=1
sum=1
while count<=20:
   if count%2!=0:
       print(count,"=odd")
   elif count%2==0:
      print(count,"=even")
   sum=sum+count
   count=count+1
print(sum,count)

