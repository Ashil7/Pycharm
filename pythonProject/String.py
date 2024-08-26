s=input("Enter string:")
n=len(s)
count1=0
count2=0
for i in range(n):
    if s[i]=='*':
        count1+=1
    elif s[i]=='#':
        count2+=1

if count1==count2:
    print("0")
elif count1>count2:
    print("Positive")
elif count1==count2==0:
    print("Invalid")
else:
    print("Negative")
