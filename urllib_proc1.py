# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 17:24:58 2017

@author: Daisy
Email: dxww01@gmail.com
Never too late or old to study!
"""

#url_quiz
import urllib2
import re
dStr = urllib2.urlopen('http://hk.finance.yahoo.com/q/cp?s=%5EDJI').read()
print dStr
m = re.findall('<tr><td class="yfnc_tabledata1"><b><a href=".*?"</a></b></td><td class="yfnc_tabledata1">(.*?)</td>.*?<b>(.*?)</b>.*?</tr>',dStr)
if m:
      print m
      print '\n'
      print len(m)
else:
      print 'not match'