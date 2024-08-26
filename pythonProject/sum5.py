a=[]
x=0
for i in range(1,26):
    if i%5==0:
        m=i
        x=x+i
        a.append(m)
print(a)
print(x)