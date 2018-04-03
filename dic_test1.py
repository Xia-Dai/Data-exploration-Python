# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 17:35:42 2017

@author: Daisy
Email: dxww01@gmail.com
Never too late or old to study!
"""

#dictionary key-value
aDict = {}.fromkeys(('wangdachui','Niuyun','linin','Tianqi'),3000)
print sorted(aDict)

pList = [('AXP','American Express','86.40'),('BA','The Boeing','122.64')]
bDict ={}
for data in pList:
      print data[2],data[0]
      bDict[data[0]] = data[2]
print (bDict) 
for i in range(2):
      name=pList[i][0]
      price=pList[i][2]
      print (name,price)
#用zip函数处理      
cDict =dict
print cDict