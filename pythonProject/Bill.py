age = []
total = 0
while len(age) < 5:
    c = int(input("1. Enter Age \n2. Exit \nEnter choice:"))
    if c == 1:
        if len(age) <= 5:
            n = int(input("Age:"))
        if n>0 and n<=17:
            age.append(n)
            total += 200
        elif n>17 and n<=40:
            age.append(n)
            total += 400
        elif n>40 and n<=120:
            age.append(n)
            total += 300
        else:
            print("Enter the age between 1-120")
    if c == 2:
        break
if len(age) >= 5:
    print("Maximum patient!!")
print("Age list:",age)
print("Total amount:",total)






