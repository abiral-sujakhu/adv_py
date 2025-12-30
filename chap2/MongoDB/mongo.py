from pymongo import MongoClient

# Connect to MongoDB server
client = MongoClient("mongodb://localhost:27017/")

# Create (or access) a database
db = client["school"]

# Create a collection and insert a document
collection = db["students"]

#inserting single data
collection.insert_one({
"id": 1,
"name": "Sita",
"marks": 85
})

#inserting multiple datas
collection.insert_many([
{"id": 2, "name": "Ram", "marks": 78},
{"id": 3, "name": "Hari", "marks": 92}
])
print("Two documents inserted successfully")

#display all
result = collection.find()
for doc in result:
    print(doc)

#just display name with sita
result = collection.find({"name": "Sita"})
# Display results with name sita 
for doc in result:
    print(doc)

# Delete one document where name is "Ram"
collection.delete_one({"name": "Ram"})
