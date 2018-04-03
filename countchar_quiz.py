# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 17:05:41 2017

@author: Daisy
Email: dxww01@gmail.com
Never too late or old to study!
"""

#count alpha
def countchar(str):
      list1 = [0]*26
      for i in range(0,len(str)):
            if (str[i] >= 'a' and str[i] <= 'z'):
                  list1[ord(str[i])-97] += 1
      print list1
if __name__ == '__main__':
      str = "Hope is a good thing."
      str = str.lower()
      countchar(str)