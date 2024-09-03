import pymongo ,re
from pymongo import errors
from datetime import datetime

client=pymongo.MongoClient("mongodb://localhost:27017/")
Db=client['HospDB']
patientCol=Db['PatientInfo']
doctorCol=Db['DoctorInfo']
bookingCol=Db['BookingInfo']

patientCol.create_index('email',unique=True)
doctorCol.create_index('phone',unique=True)

date=datetime.now().strftime('%d-%m-%y')

def patientLogin():
    print("\n********* LOGIN ***********")
    id=input("\nEnter your OP NO. :")
    while True:
        if re.findall(r'\b\d{4}\b',id):
            break
        else:
            print("Invalid!!")
            id=input("Enter Valid OP No.(4 Digits):")
    query={'_id':int(id)}
    pwd=input("Enter your password:")
    result=patientCol.find_one(query)
    if result:
        if result['password']==pwd:
            print("Login Success")
            docInfo(id)
            
        else:
            print("Wrong password!!")
    else:
        print(f'OP No. {id} not found!!!')

def docLogin():
    print("\n********* LOGIN ***********")
    phone=input("\nEnter your phone number:")
    while True:
        if re.findall(r'^\d{10}$', phone):
            break
        else:
            print("Invalid phone number")
            phone=input("Enter valid phone number:")
    pwd=input("Enter your password:")
    query={'phone':phone}
    result=doctorCol.find_one(query)
    if result:
        if result['password']==pwd:
            print("\nLogin success!!")
            id=result['_id']
            patientList(id)
        else:
            print("Wrong password")
    else:
        print("Record not found")

def patientList(id):
    print("\n***** Patient list *****")
    docId=str(id)
    query={'doctorId':docId, 'date':date}
    result=bookingCol.find(query).sort([('token',1)])
    if result is None:
        for x in result:
            patId=x['patientId']
            query1={'_id': int(patId)}
            res=patientCol.find_one(query1)

            if res:
                print(f"\n**** Token no {x['token']} ****")
                print('Name:',res['name'])
                print('Age:',res['age'])
                print("Gender:",res['gender'])
                print('Phone:',res['phone'])
                print('Address:',res['address'] +"\n")

            else:
                print("Invalid")
    else:
        print("\nNo Appointments!!")


def docInfo(id):
    patientId=id
    ch = int(input("\n1.Cardiologist\n2.Neurologist\n3.Dermatologist\nChoose your department:"))
    if ch==1:
        dept='cardiologist'
    elif ch==2:
        dept='neurologist'
    elif ch==3:
        dept='dermatologist'
    else:
        print("Invalid!!")

    query={'department':dept}
    result=doctorCol.find(query)
    count=1
    for x in result:
        print(f'\n{count}.Doctor Id:',x['_id'])
        print("  Name: Dr.",x['name'])
        print('  Phone:',x['phone'])
        print("  Department:",x['department'])
        count+=1
    if count>0:
        docId=input("\nEnter doctor Id to consult:")
        query1={'_id':int(docId)}
        res=doctorCol.find_one(query1)
        last_id = bookingCol.find_one({'doctorId':str(docId),'date':date},sort=[('token', -1)])
        if last_id:
            token = last_id['token'] + 1
        else:
            token = 1

        dict3={
            'token':token,
            'patientId':patientId,
            'doctorId':docId,
            'date':date
        }
        if res:
            query2={'patientId':patientId,'doctorId':str(docId),'date':date}
            if bookingCol.find_one(query2):
                print("\nAlready booked")
            else:
                print("\nBooking confirmed!!")
                bookingCol.insert_one(dict3)
                print(f'Your TOKEN NO. {token}')
        else:
            print("\nDoctor not found!!")
    else:
        print("\nNo Doctors Available")

def docRegister():
    name = input("Enter your name:")
    while True:
        if re.findall(r'^[a-zA-Z]+$', name):
            break
        else:
            print("Name should not contain numbers")
            name = input("Enter name again:")
    ch=int(input("\n1.Cardiologist\n2.Neurologist\n3.Dermatologist\nChoose your department:"))
    if ch==1:
        dept="cardiologist"
    elif ch==2:
        dept='neurologist'
    elif ch==3:
        dept='dermatologist'
    else:
        print("Invalid choice!!")

    phone = input("Enter phone number:")
    while True:
        if re.findall(r'^\d{10}$', phone):
            break
        else:
            print("Phone number contain only digits!!")
            phone = input("Enter phone number again:")
    pwd=input("Enter password:")
    while True:
        password_pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
        if re.match(password_pattern, pwd):
            break
        else:
            print("\nInvalid password:")
            print("* Password should be at least 8 characters long")
            print("* Password should contain at least one lowercase letter, one uppercase letter, one digit, and one special character")
            pwd = input("Enter your password again: ")

    last_id = doctorCol.find_one(sort=[('_id', -1)])
    if last_id:
        id = last_id['_id'] + 1
    else:
        id = 111
    dictDoc={
        '_id':id,
        'name':name,
        'department':dept,
        'phone':phone,
        'password':pwd
    }
    try:
        doctorCol.insert_one(dictDoc)
        print("Registered Successfully!!\n")
    except errors.DuplicateKeyError:
        print("Phone number already exists")

def patientRegister():

    name = input("Enter your name:")
    while True:
        if re.findall(r'^[a-zA-Z]+$',name):
            break
        else:
            print("Name should not contain numbers")
            name=input("Enter name again:")

    age=input("Your Age:")
    while True:
        if re.findall(r'\d{1,2}',age):
            age=int(age)
            if age>=0 and age<=100:
                break
            else:
                print("Enter Valid age!!")
                age=input("Enter age again:")
        else:
            print("Enter Valid age!!")
            age = input("Enter age again:")

    gender = input("Gender(Male/Female/Other):")
    while True:
        gen = gender.lower()
        if gen == 'male' or gen == 'female' or gen == 'other':
            break
        else:
            print("Enter valid gender")
            gender = input("Gender(Male/Female/Other):")

    phone=input("Enter phone number:")
    while True:
        if re.findall(r'^\d{10}$',phone):
            break
        else:
            print("Phone number contain only digits!!")
            phone=input("Enter phone number again:")

    email=input("Enter Email:")
    while True:
        if re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]",email):
            break
        else:
            print("Enter valid email ID")
            email=input("Enter Email Id again:")

    addr=input("Enter your address:")
    while True:
        if addr=='':
            print("Address cannot be empty")
            addr=input("Enter your address:")
        else:
            break

    pwd = input("Enter your password: ")
    while True:
        password_pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
        if re.match(password_pattern, pwd):
            break
        else:
            print("\nInvalid password:")
            print("* Password should be at least 8 characters long")
            print("* Password should contain at least one lowercase letter, one uppercase letter, one digit, and one special character")
            pwd = input("Enter your password again: ")

    last_id=patientCol.find_one(sort=[('_id',-1)])
    if last_id:
        id=last_id['_id']+1
    else:
        id=1111

    dict={
        '_id':id,
        'name':name,
        'age':age,
        'gender':gender,
        'phone':phone,
        'email':email,
        'address':addr,
        'password':pwd
    }
    try:
        patientCol.insert_one(dict)
        print(f"\nPatient successfuly registered!!\n\nPatient OP NO. is {id}\n(**Use this OP NO. to login**)\n")
    except errors.DuplicateKeyError:
        print("Email-Id  already Exists")

while True:
    print("\n1.Patient\n2.Doctor")
    c=int(input("Enter choice:"))
    if c==1:
        print("1.Patient LogIn\n2.Patient Register")
        ch=int(input("Enter choice:"))
        if ch==1:
            patientLogin()
        elif ch==2:
            patientRegister()
    elif c==2:
        print("1.Doctor Registration\n2.Doctor Login")
        ch=int(input("Enter choice:"))
        if ch==1:
            docRegister()
        elif ch==2:
            docLogin()
