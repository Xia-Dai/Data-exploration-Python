# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 16:08:05 2017

@author: Daisy
Email: dxww01@gmail.com
Never too late or old to study!
"""
# url 网页获取数据
import urllib
r = urllib.urlopen('https://www.google.com/')
html = r.read()
print html