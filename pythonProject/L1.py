a=[]
for i in range(1,21):
    a.append(i)
print("List:",a)
for i in range(len(a)):
    if a[i]%2!=0:
        a[i]='&'
print("ODD LIST:",a)
a.reverse()
print("Reversed List:",a)
