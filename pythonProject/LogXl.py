import pandas as pd,os
def create(): #function to create dataframe and to insert in excel file

    name=str(input("Name:"))
    pwd=str(input("Pass:"))
    df=pd.DataFrame({'Names':[name],'Password':[pwd]}) #data is inserted in the form of dictionary
    if os.path.isfile('log3.csv'): #check whether file exists or not
        df.to_csv('log3.csv',mode='a',index=False,header=False) #append data to excel file if the file already exists
    else:
        df.to_csv('log3.csv',header=True,index=False)#create new excel file and insert data

def check(): # function to check the input given by user present in the excel file
    n=str(input("name:"))
    p=str(input("pass:"))
    df=pd.read_csv('log3.csv') #read excel file
    if n in df['Names'].values and p in df['Password'].values:
        print("Log-in Successful")
    else:
        print("Not matching")

while True:
    c = int(input("1. REGISTER \n2. LOGIN \n3. Exit \nChoice: "))
    if c == 1:
        create()
    elif c==2:
        check()
    elif c == 3:
        break
