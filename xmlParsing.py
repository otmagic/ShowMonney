#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Notes  : 获取最新验证码数据信息
# @Time  : 2019-07-30 00:04
# @Author: OTMAGIC
# @File  : xmlParsing.py

import json
import xmltodict
import pymongo

# 时间处理
import time

# 本地时间
localTime = time.strftime("%Y%m%d%H%M%S")

# 定义xml转json的函数
xml_file = open('/Volumes/work/pythonSpace/ShowMoney/data/A_Verification.xml', encoding='utf-8')
xml_str = xml_file.read()

# parse是的xml解析器e = xmlDom.parse(xmlstr)
xmlParse = xmltodict.parse(xml_str)

# json库dumps()是将dict转化成json格式，loads()是将json转化成dict格式。
# dumps()方法的ident=1，格式化json
jsonStr = json.dumps(xmlParse).replace('@', '')

myClient = pymongo.MongoClient('mongodb://localhost:27017/')
DB_List = myClient.list_database_names()

insertTime = {"$set": {"insertTime": localTime}}

if "showMoney" in DB_List:
    print("---------- 数据库已存在！----------")
    myDB = myClient['showMoney']
    colList = myDB.list_collection_names()
    if "codeInfo" in colList:  # 判断 sites 集合是否存在
        print("---------- 集合已存在！----------")

        myCol = myDB["codeInfo"]
        i = myCol.insert_one(json.loads(jsonStr))
        myCol.update_one(json.loads(jsonStr), insertTime)
        print(i.modified_count, "文档已修改")

        for x in myCol.find():
            print(x)
            p1 = {}  # 空字典
            if x == p1:
                print(1)
            else:
                print(2)

    else:
        print('---------- 集合不存在！----------')
else:
    print('---------- 数据库不存在！----------')
