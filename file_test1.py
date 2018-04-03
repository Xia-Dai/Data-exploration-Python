# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 15:12:19 2017

@author: Daisy
Email: dxww01@gmail.com
Never too late or old to study!
"""
#在字符串前加r是防止字符串转义如出现\t
f = open(r'c:\users\daixia\python_prac\firstfile.txt','w')
f.write('Hello, World!')
f.close()
#读文件
f = open(r'firstfile.txt','r')
p1 = f.read(5)
p2 = f.read()
print p1,p2
#读出文件内容
f = open(r'C:\Users\Daixia\python_prac\companies.txt')
cNames = f.readlines()
print cNames
f.close
#在如上companies 文件的每行内容前加上序号

f1 = open(r'C:\Users\Daixia\python_prac\companies.txt')
cNames = f1.readlines()
for i in range(0,len(cNames)):
      cNames[i] = str(i+1) + '' +cNames[i]
f1.close()
f2 = open(r'C:\Users\Daixia\python_prac\scompanies.txt','w')
f2.writelines(cNames)
f2.close()