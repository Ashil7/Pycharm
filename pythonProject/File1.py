import re,os
def create():
    empName=input("Enter name:")
    flag=0
    while flag==0:
        if re.findall("[0-9]",empName):
            print("Name should contain only Alphabets")
            empName=input("Enter Name again:")
        else:
            flag=1

    if os.path.isfile(empName):
        print("File already exists")
        exit()
    else:
        f=open(empName,'a')
        f.write(empName)

    empMail=input("Enter mail ID:")
    flag=0
    while flag==0:
        if re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]",empMail):
            f.write('\n'+empMail)
            flag=1
        else:
            print("Invalid email address")
            empMail=input("Enter mail again:")

    empPhone=input("Enter Phone Number:")
    flag=0
    while flag==0:
        if re.findall(r'^\d{10}$',empPhone):
            f.write('\n'+empPhone)
            print("File created Successfully...")
            flag=1
        else:
            print("Invalid phone number")
            empPhone=input("Enter number again:")
    f.close()
def delete():
    a=input("Enter the name of the file to be removed:")
    if os.path.isfile(a):
        os.remove(a)
        print("deleted!!")

    else:
        print("File not found!!")
def read():
    name=input("Enter name of the file:")
    if os.path.isfile(name):
        print("*******************************")
        f=open(name,'r')
        print(f.read())
        print("*******************************")
    else:
        print("File not found")

while True:
    c=int(input("1. Create File \n2. Delete file \n3. Read File \n4. Exit \nEnter Choice:"))
    if c==1:
        create()
    elif c==2:
        delete()
    elif c==3:
        read()
    elif c==4:
        break
    else:
        print("Invalid Choice")





