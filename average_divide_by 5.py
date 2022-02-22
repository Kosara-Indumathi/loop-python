# Take input of weights of 11 people and then print their average and then check whether the average weight is a multiple of 5 or not? This means that when you will divide the average weight by 5, the remainder should be 0.
i=1
sum=0
while i<=11:
    weight=int(input("enter weights"))
    sum=sum+weight
    i=i+1
    avarage=sum/11
print(sum)
if avarage%5==0:
    print(avarage)
    
