a=[1,2,2,4,5,5,9,9,7]
a.sort()
b=[]
n=len(a)
'''for i in range(n):
    count=0
    for j in range(n):
        if a[i]==a[j]:
            count=count+1
    if count==1:
        b.append(a[i])'''

for i in range(n):
    c=a.count(a[i])
    if c==1:
        b.append(a[i])

print(b)
print("Number of unique elements:",len(b))