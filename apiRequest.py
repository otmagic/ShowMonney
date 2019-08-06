#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time  : 2019-07-30 00:04
# @Author: OTMAGIC
# @File  : apiRequest.py

# 导入requests包
import requests
# 导入mongoDB包
import pymongo
# json 解析依赖包
import json

# 请求头部定制
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0',
    'Host': 'www.cwl.gov.cn',
    'Referer': 'http://www.cwl.gov.cn/kjxx/ssq/kjgg/',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip,deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cookie': 'Sites=_21; UniqueID=uPRArZvNUpMS2Vcn1564410802239; _ga=GA1.3.1164378687.1564410803; _gid=GA1.3.1671824908.1564410803; 21_vq=17'
}

# 1. 组装请求
url = "http://www.cwl.gov.cn/cwl_admin/kjxx/findDrawNotice?name=ssq&issueCount=30"  # 这里只有url，字符串格式

# 2. 发送请求，获取响应
res = requests.get(url, headers=header)  # res即返回的响应对象

# 3. 解析响应
rs = res.text
print(rs)  # 输出响应的文本

myClient = pymongo.MongoClient("mongodb://localhost:27017/")
myDB = myClient["showMoney"]
myCol = myDB["apiRequests"]

x = myCol.insert_one(res.json())

# 输出插入的所有文档对应的 _id 值
json = json.loads(rs)
print(json['state'])
