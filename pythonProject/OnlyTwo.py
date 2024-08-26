a=[1,2,2,4,5,5,9,9,7]
a.sort()
b=[]
n=len(a)
for i in range(n):
    c=a.count(a[i])
    if c==2:
        b.append(a[i])
print(b)
