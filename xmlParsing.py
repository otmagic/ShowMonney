#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Notes  : 获取最新验证码数据信息
# @Time  : 2019-07-30 00:04
# @Author: OTMAGIC
# @File  : xmlParsing.py

import json
import xmltodict
import pymongo

# 定义xml转json的函数
def xmltojson():
    xml_file = open('/Volumes/work/pythonSpace/ShowMoney/data/A_Verification.xml', encoding='utf-8')
    xml_str = xml_file.read()

    # parse是的xml解析器e = xmlDom.parse(xmlstr)
    xmlParse = xmltodict.parse(xml_str)

    # json库dumps()是将dict转化成json格式，loads()是将json转化成dict格式。
    # dumps()方法的ident=1，格式化json
    jsonStr = json.dumps(xmlParse).replace('@', '')

    # 解析响应
    rs = jsonStr.text
    print(rs)  # 输出响应的文本

    myClient = pymongo.MongoClient("mongodb://localhost:27017/")
    myDB = myClient["showMoney"]
    myCol = myDB["apiRequests"]

    x = myCol.insert_one(jsonStr.json())

    print(x)

if __name__ == "__main__":
    xmltojson()  # 调用转换函数
