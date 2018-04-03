# -*- coding: utf-8 -*-
"""
Created on Thu Mar 08 17:26:19 2018

@author: Daisy
Email: dxww01@gmail.com
Never too late or old to study!
"""

def factorial(x):
  if x == 0 or x == 1:
    return 1
  else:
    return x * factorial(x-1)

print factorial(4)


score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10}

def scrabble_score(word):
  s = 0
  for i in word:
    for key in score:
      if i.lower() == key:
        s += score[key]
  return s
  
def censor(text, word):
  words = text.split()
  result = ''
  stars = '*' * len(word)
  count = 0
  for i in words:
    if i == word
      words[count] = stars
      count += 1
  result =' '.join(words)

  return result