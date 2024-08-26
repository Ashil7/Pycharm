import random

n=random.randint(1,10)
i=1
print(n)
while i<=3:
    num = int(input("Enter the a number between:"))
    if n==num:
        print("You WON!!")
        break
    elif i==3:
        print("You Lose!!")
        break
    elif num<n:
        print("HINT : Choose greater")
        i+=1
    elif num>n:
        print("HINT : Choose Lesser")
        i+=1







