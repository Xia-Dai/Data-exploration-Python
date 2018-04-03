# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 16:23:46 2017

@author: Daisy
Email: dxww01@gmail.com
Never too late or old to study!
"""

f = open(r'C:\Users\Daixia\python_prac\Blowing in the wind.txt','r+')
Poem = f.readlines()
print f.tell()
f.seek(0,0)
Poem = ["Blowin' in the wind\n"]+ Poem
print Poem
print f.tell()
print type(Poem)
Poem.insert(1,"Bob Dylan\n")
print Poem
f.seek(0,2)
Poem= Poem + ["\n1962 by Warner Bros. Inc."]
print Poem
f.close()
f = open(r'C:\Users\Daixia\python_prac\Blowing in the wind.txt','w+')
f.writelines(Poem)
f.seek(0,0)
Poem = f.readlines()
print Poem
f.close()