#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#@Time  : 2019-07-30 23:43
#@Author: OTMAGIC
#@File  : db.py


from xml.etree import ElementTree as et
import json


def readxml_et():
  tree = et.ElementTree(file="/Volumes/work/workspace/ShowMoney/data/A_SetTable.xml")
  root = tree.getroot()
  A = dict()
  listbigoption = []
  for child_root in root:
    if child_root.tag == 'filename':
      imagePath = child_root.text
    if child_root.tag == 'object':
      listobject = dict()
      for xylabel in child_root:
        if xylabel.tag == 'name':
          label = xylabel.text
        if xylabel.tag == 'polygon':
          listpoints = []
          for pt in xylabel:
            if pt.tag == 'pt':
              listxy = []
              for i in pt:
                if i.tag == 'x':
                  listxy.append(int(i.text))
                if i.tag == 'y':
                  listxy.append(int(i.text))
                listpoints.append(listxy)
          listobject['points'] = listpoints
          listobject['line_color'] = 'null'
          listobject['label'] = label
          listobject['fill_color'] = 'null'
          listbigoption.append(listobject)
        # print(listbigoption)
  A['lineColor'] = [0, 255, 0, 128]
  A['imageData'] = 'imageData'
  A['fillColor'] = [255, 0, 0, 128]
  # A['imagePath'] = imagePath
  A['shapes'] = listbigoption
  A['flags'] = {}
  with open('1.json', 'w') as f:
    json.dump(A, f)


readxml_et()

rs = readxml_et()
print(rs)  # 输出响应的文本