list=['a','c','b','a','c','c']
list2=[]
count=0
for i in range(len(list)):
    for j in range(len(list)):
        if list[i]==list[j]:
            count+=1
        if count>=2:
            list2.append(list[i])
            count=0
t1=set(list2)
print(t1)
print("count:",len(t1))