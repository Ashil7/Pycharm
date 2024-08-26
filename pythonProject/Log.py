dict={}
print("\n------ Register ------\n")
dict['name']=input("Enter name:")
dict['pass']=input("Enter password:")
print(dict)
print("\n")


print("------- Enter your credentials to login ------\n")
name=input("Enter name:")
pas=input("Enter Password:")

if name==dict['name'] and pas==dict['pass']:
    print("Login Success!!")
else:
    print("Login failed!!")