#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#@Time  : 2019-07-30 23:43
#@Author: OTMAGIC
#@File  : db.py

import pymongo

myClient = pymongo.MongoClient("mongodb://10.1.1.224:27017/")
myDB = myClient["showMoney"]
myCol = myDB["sites"]

myDict = {"name": "showMoney", "alexa": "10000", "url": "https://www.runoob.com"}

mylist = [
  { "_id": 1, "name": "RUNOOB", "cn_name": "菜鸟教程"},
  { "_id": 2, "name": "Google", "address": "Google 搜索"},
  { "_id": 3, "name": "Facebook", "address": "脸书"},
  { "_id": 4, "name": "Taobao", "address": "淘宝"},
  { "_id": 5, "name": "Zhihu", "address": "知乎"}
]

x = myCol.insert_many(mylist)

# 输出插入的所有文档对应的 _id 值
print(x.inserted_ids)
