a=int(input("a:"))
b=int(input("b:"))
c=int(input("c:"))

if a>b and a>c:
    print('a is largest')
elif b>a and b>c:
    print('b is largest')
elif a==b==c:
    print("All equal")
else:
    print('c is largest')