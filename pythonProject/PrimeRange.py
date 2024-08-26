a=[]
n=int(input("Limit:"))

for i in range(1,n):
    count=0
    for x in range(1,i+1):
        if i%x==0:
            count=count+1
    if count==2:
        a.append(i)

print(a)

