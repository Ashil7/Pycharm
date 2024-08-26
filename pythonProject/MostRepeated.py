a=[1,3,3,3,4,4,5,2]
mostRepeated=0
maxCount=0
for i in range(len(a)):
    count=a.count(a[i])
    if count>maxCount:
        mostRepeated=a[i]
        maxCount=count
print("Most repeated element:",mostRepeated," \nNumber of times repeated:",maxCount)