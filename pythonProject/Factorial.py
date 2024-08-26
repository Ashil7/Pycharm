def fact(n):
    if n<0:
        print("Not possible")
    elif n==0:
        return 1
    else:
        result=n*fact(n-1)
        return result


n=int(input("enter number:"))
print(fact(n))