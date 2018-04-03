# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 20:46:34 2018

@author: Daisy
Email: dxww01@gmail.com
Never too late or old to study!
"""

def word_count(word):
      count = 0
      lib = {}
      new_word = word.split()
      for i in new_word:
            if i not in lib:
                  lib[i] = 1
            else:
                  lib[i] =lib[i] +1

      return lib
print word_count("I am from China")
      