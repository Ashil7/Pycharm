a = int(input("Enter Number 1:"))
b = int(input("Enter Number 2:"))
while True:

    print(" 1. Add \n 2. Sub \n 3. Multi \n 4. Div \n 5. Exit \n")
    c=int(input("Enter Choice:"))
    if c==1:
        print("Ans:",a+b)
    elif c==2:
        print("Ans:",a-b)
    elif c==3:
        print("Ans:",a*b)
    elif c==4:
        print("Ans:",a/b)
    elif c==5:
        break
    else:
        print("Choose between 1-5:")

