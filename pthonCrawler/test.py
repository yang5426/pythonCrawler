import pymongo

MONGO_CONNECTION_STRING = 'mongodb://localhost:27017'
MONGO_DB_NAME = 'movies'
MONGO_COLLECTION_NAME = 'movies'
client = pymongo.MongoClient(MONGO_CONNECTION_STRING)
db = client['movies']
collection = db['movies']

print('find 方法 多条查询')
results = collection.find()
print(results)
for result in results:
    print(result)

print("计数")
count = collection.find().count()
print(count)