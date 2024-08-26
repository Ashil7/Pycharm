count=0
l=['mom','dad','abc']
for x in l:
    if len(x)>2 and x[0]==x[-1]:
        count+=1
print(count)

