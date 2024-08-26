
l=['a','b','c','a','a','b']
a=[]
for i in range(len(l)):
    if l.count(l[i])>=2:
        a.append(l[i])

print(a)
for i in a:
    for j in range(len(l)):
        if l[j]==i:
            l[j]='x'
print(l)