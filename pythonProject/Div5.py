a=[]
b=[]
for i in range(0,50):
    a.append(i)
print(a)

for i in a:
    if a[i]%5==0:
        b.append(a[i])

print(b)

s=0

for i in range(len(b)):
    s=s+b[i]
print(s)