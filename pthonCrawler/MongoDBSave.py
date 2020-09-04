import pymongo
client = pymongo.MongoClient(host='localhost', port=27017)
db = client.test
# db = client['test']

collection = db.students
# collection = db['students']

student = {
    'id': '20170101',
    'name': 'Jordan',
    'age': 20,
    'gender': 'male'
}
# result = collection.insert(student)
# print(result)


student1 = {
    'id': '20170101',
    'name': 'Jordan',
    'age': 20,
    'gender': 'male'
}

student2 = {
    'id': '20170202',
    'name': 'Mike',
    'age': 21,
    'gender': 'male'
}

# result = collection.insert([student1, student2])
# print(result)


student = {
    'id': '20170101',
    'name': 'Jordan',
    'age': 20,
    'gender': 'male'
}

# result = collection.insert_one(student)
# print(result)
# print(result.inserted_id)



student1 = {
    'id': '20170101',
    'name': 'Jordan',
    'age': 20,
    'gender': 'male'
}

student2 = {
    'id': '20170202',
    'name': 'Mike',
    'age': 21,
    'gender': 'male'
}

# result = collection.insert_many([student1, student2])
# print(result)
# print(result.inserted_ids)


print('查询')
result = collection.find_one({'name': 'Mike'})
print(type(result))
print(result)


# 根据 ObjectId 来查询，此时需要调用 bson 库里面的 objectid
from bson.objectid import ObjectId
result = collection.find_one({'_id': ObjectId('5f4f3afc00bf77e47d030070')})
print(result)

print()
print('find 方法 多条查询')
results = collection.find({'age': 20})
print(results)
for result in results:
    print(result)

results = collection.find({'age': {'$gt': 20}})
results = collection.find({'name': {'$regex': '^M.*'}})
for result in results:
    print(result)


print("计数")
count = collection.find().count()
print(count)

count = collection.find({'age': 20}).count()
print(count)

print('排序')
results = collection.find().sort('name', pymongo.ASCENDING)
print([result['name'] for result in results])
results = collection.find().sort('name', pymongo.DESCENDING)
print([result['name'] for result in results])

print('偏移')
results = collection.find().sort('name', pymongo.ASCENDING).skip(8).limit(2)
print([result['name'] for result in results])

# 数据量非常庞大的时候
results = collection.find({'_id': {'$gt': ObjectId('5f4f3b9fb8594a94a9effe96')}})
print([result['name'] for result in results])


# 如果不用 $set 的话，则会把之前的数据全部用 student 字典替换；如果原本存在其他字段，则会被删除。
print('更新')
condition = {'name': 'Jordan'}
student = collection.find_one(condition)
student['age'] = 25
result = collection.update_one(condition, {'$set': student})
print(result)
print(result.matched_count, result.modified_count)


condition = {'age': {'$gt': 20}}
result = collection.update_many(condition, {'$inc': {'age': 1}})
print(result)
print(result.matched_count, result.modified_count)


print('删除')
result = collection.remove({'name': 'Kevin'})
print(result)
result = collection.delete_one({'name': 'Kevin'})
print(result)
print(result.deleted_count)
result = collection.delete_many({'age': {'$lt': 25}})
print(result.deleted_count)


# PyMongo 还提供了一些组合方法，如 find_one_and_delete、find_one_and_replace 和 find_one_and_update，它们分别用于查找后删除、替换和更新操作

# 我们还可以对索引进行操作，相关方法有 create_index、create_indexes 和 drop_index
