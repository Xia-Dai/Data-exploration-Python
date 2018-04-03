# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 15:44:34 2017

@author: Daisy
Email: dxww01@gmail.com
Never too late or old to study!
"""
f1 = open(r'C:\Users\Daixia\python_prac\companies.txt')
cNames = f1.readlines()
for i in range(0,len(cNames)):
      cNames[i] = str(i+1) + ' ' +cNames[i]
f1.close()
f2 = open(r'C:\Users\Daixia\python_prac\scompanies.txt','w+')
f2.writelines(cNames)
#若想直接读取数据需要把文件指针调整一下
print f2.tell()
f2.seek(8)
print f2.tell()
cNames2 = f2.readlines()
print cNames2
f2.close()
#f3 = open(r'C:\Users\Daixia\python_prac\scompanies.txt','r')
#cNames2 = f3.readlines()
#print cNames2
#f3.close()