# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 15:50:42 2017

@author: Daisy
Email: dxww01@gmail.com
Never too late or old to study!
"""

#dict_test2 格式化字符串
aInfo = {'Wangdachui':3000, 'Niuyun': 2000, 'Linling': 4500, 'Tianqi': 8000}
for key in aInfo.keys():
      print 'name = %s, salary = %s' %(key, aInfo[key])
"Niuyun's salary is %(Niuyun)s." %aInfo
# %(key)格式说明符 % 字典对象名
template ='''
   Welcome to the pay wall.
   Niuyun's salary is %(Niuyun)s.
   Wangdachui's salary is %(Wangdachui)s
   '''
print template % aInfo
print aInfo.keys()
print aInfo.values()

aInfo['Wang']
print aInfo.get('Wang') #查找某key是否在字典里

# built_in functions
bInfo = {'Wangdachui': 4000,'Niuyun': 9000, 'Wangzi': 6000}
aInfo.update(bInfo) #更新表aInfo
print aInfo

#删除 {}赋值给对象
aStock ={'AXP':86.40, 'BA':122.64}
bStock = aStock
aStock = {} 
print aStock, bStock #bStock不会被清空

#清空原有对象，被赋值的对象也被清空
aStock ={'AXP':86.40, 'BA':122.64}
bStock = aStock
aStock.clear()
print aStock, bStock



