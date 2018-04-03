# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 16:28:38 2017

@author: Daisy
Email: dxww01@gmail.com
Never too late or old to study!
"""

#元组 tuple 不可赋值改变 list可以
aTuple = (1,9,0,20)
sorted(aTuple)
#在映射类型中当作键来使用
#函数的特殊类型参数
#作为很多内建函数的返回值

def func(args1,*argst):
      print args1
      print argst
func("Hello","Wangdachui","Liuyun")