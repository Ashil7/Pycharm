import pymongo
from pymongo import errors

client=pymongo.MongoClient('mongodb://localhost:27017/')
db=client['Db_info']
col=db['info']

col.create_index("phone", unique=True)
def create(): #Insert data
    name=input("Enter Username:")
    addr=input("Enter Address:")
    phone=input("Enter Phone Number:")
    pwd=input("Enter Password:")

    dict={
        'name': name,
        'address': addr,
        'phone': phone,
        'Password': pwd
    }
    try:
        col.insert_one(dict)
        print("Data inserted!!")
    except errors.DuplicateKeyError:
        print(f"Error: Phone number {phone} already is use.")
def update():#update data
    phone=input("Enter Phone number:")
    query={"phone":phone}
    x=col.find_one(query)
    if x:
        print("1. Name \n2. Address\n3. Phone\n4. Password\n5. Exit")
        c=int(input("Enter choice:"))
        if c==1:
            name=input("Enter New Username:")
            newQuery={'$set':{'name': name}}
            col.update_one(query,newQuery)
            print("Username updated!!")
        elif c==2:
            addr=input("Enter new Address:")
            newQuery={'$set':{'address':addr}}
            col.update_one(query,newQuery)
            print("Address updated!!")
        elif c==3:
            phn=input("Enter new phone number:")
            newQuery={'$set':{'phone':phn}}
            try:
                col.update_one(query,newQuery)
                print("Phone number updated!! ")
            except errors.DuplicateKeyError:
                print(f"Phone number {phn} already exists.")
        elif c==4:
            nPwd=input("Enter new password:")
            newQuery={'$set':{'Password':nPwd}}
            col.update_one(query,newQuery)
            print("Password updated!!")
        elif c==5:
            exit()
        else:
            print("Invalid choice!!")
def delete(): #delete record
    phn=input("Enter phone number:")
    query={'phone':phn}
    result=col.find_one(query)
    if result:
        col.delete_one(query)
        print("Record deleted!!")
    else:
        print("Record not found!!")
def read(): #view data
    phn = input("Enter phone number:")
    query = {'phone': phn}
    result=col.find_one(query)
    if result:
        print("*************************")
        print("Name:",result['name'])
        print("Address:",result['address'])
        print("Phone:",result['phone'])
        print("Password:",result['Password'])
        print("*************************")
    else:
        print("Record not found!!")

while True:
    print('1.Create \n2.Update \n3.Delete \n4.Read\n5.Exit')
    c=int(input("Enter choice:"))
    if c==1:
        create()
    elif c==2:
        update()
    elif c==3:
        delete()
    elif c==4:
        read()
    elif c==5:
        exit()
    else:
        print("Invalid choice!!")