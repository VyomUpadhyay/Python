from pymongo import mongo_client, MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["mydb"]
collection = db["movie"]

all_movies= collection.find()
print("All Movies: ")
for e1 in all_movies:
    print(e1)