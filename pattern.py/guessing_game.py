n=5
user=int(input("enter the number"))
while user<=10:
    if user!=5:
        user1=int(input("enter the number"))
        if user1!=n:
            i=0
            while i<n:
                user=int(input("enter number"))
                if user==n:
                    print("you win the game congrats")
                elif i==n:
                    print("you loss the game")
                    break
                i=i+1
        else:
            print("your guess is right")
                
    else:
        print("your right")
        break


    