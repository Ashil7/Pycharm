a=[]
for i in range(1,11):
    a.append(i)
print("LIST:",a)
for i in range(len(a)):
    if a[i]%7==0:
        a[i]='%'
    elif a[i]%2==0:
        a[i]='@'
t=tuple(a)
print(t)