from pymongo import mongo_client, MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["mydb"]
collection = db["movie"]

all_myemployees = collection.find()
print("All Movies: ")
for e1 in all_myemployees:
    mname=e1["MNAME"]
    hero=e1["HERO"]
    ryear=e1["RYEAR"]
    income=e1["INCOME"]
    budget=e1["BUDGET"]
    print(mname,"\t",hero,"\t",ryear,"\n",income,"\t",budget)

