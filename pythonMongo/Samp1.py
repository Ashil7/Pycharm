import pymongo

client=pymongo.MongoClient("mongodb://localhost:27017/")
db=client['Db1']
col=db['Doc1']

'''list=[
  { "name": "Amy", "address": "Apple st 652"},
  { "name": "Hannah", "address": "Mountain 21"},
  { "name": "Michael", "address": "Valley 345"},
  { "name": "Sandy", "address": "Ocean blvd 2"},
  { "name": "Betty", "address": "Green Grass 1"},
  { "name": "Richard", "address": "Sky st 331"},
  { "name": "Susan", "address": "One way 98"},
  { "name": "Vicky", "address": "Yellow Garden 2"},
  { "name": "Ben", "address": "Park Lane 38"},
]
a=col.insert_many(list)'''


x=col.find({},{'name':1, '_id':0})
for i in x:
    print(i)
