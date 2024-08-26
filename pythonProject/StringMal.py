s=input("Enter string:")
b=''
for i in s:
    if i in ("!",'@','#','$','%','&','*'):
        continue
    else:
        b+=i
print(b)
