


import pymongo


myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient['stu']     # 建立数据库
col = mydb['col']       # 建立集合
"""增加数据"""
# 插入单个数据
# mydict1 = { "name": "RUNOOB", "alexa": "10000", "url": "https://www.runoob.com" }
# x = col.insert_one(mydict1)
# print(x.inserted_id)
# 插入多个数据
# mylist2 = [
#   { "name": "Taobao", "alexa": "100", "url": "https://www.taobao.com" },
#   { "name": "QQ", "alexa": "101", "url": "https://www.qq.com" },
#   { "name": "Facebook", "alexa": "10", "url": "https://www.facebook.com" },
#   { "name": "知乎", "alexa": "103", "url": "https://www.zhihu.com" },
#   { "name": "Github", "alexa": "109", "url": "https://www.github.com" }
# ]
# y = col.insert_many(mylist2)
# print(y.inserted_ids)

# 确认集合是否在数据库中
# collist = mydb. list_collection_names()    # 返回库中所有集合的列表
# print(collist)
"""查询数据"""
# print(col.find_one())    #find_one() 方法来查询集合中的一条数据
#
# for each in col.find():    # find() 方法可以查询集合中的所有数据
#     print(each)
#
# for each in col.find({},{'_id':0,'name':1}):   # 通过find()指定查询同时指定0,1，报错{'_id':0,'name':1,'alexa':0})
#     print(each)

# for each in col.find({"alexa":{"$gt":"100"}},{'_id':0}):    # find(<{条件}>,<{输出形式}>)    通过修饰附条件  查询数据
#     print(each)

# for each in col.find({"name":{"$regex":'^T'}}):      # 通过正则  查询数据
#     print(each)

# for each in col.find().limit(3):      # 限制查询数目
#     print(each)

"""修改数据"""


# query = {'alexa': '101'}
# new_value  = {'alexa': '1000'}
# col.update_one(query,{"$set":new_value})       #   查找    修改。。。。
# for each in col.find():
#     print(each)


# query = {'name':{"$regex":'^Q'}}
# new_value = {'name':'qq'}
# col.update_one(query,{"$set":new_value})       #   查找    修改。。。
# for each in col.find():
#     print(each)



"""文档删除"""

col.delete_many()
col.delete_many()      # 查找  删除。。。