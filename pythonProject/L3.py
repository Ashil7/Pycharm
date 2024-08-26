a=[]
for i in range(1,11):
    a.append(i)
print("LIST:",a)
s=0
for i in range(len(a)):
    if a[i]%2==0 and a[i]%3==0:
        continue
    else:
        s+=a[i]

print(s)