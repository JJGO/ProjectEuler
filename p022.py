#!/usr/bin/env python

"""
Project Euler Problem 22
========================

   Using [1]names.txt, a 46K text file containing over five-thousand first
   names, begin by sorting it into alphabetical order. Then working out the
   alphabetical value for each name, multiply this value by its alphabetical
   position in the list to obtain a name score.

   For example, when the list is sorted into alphabetical order, COLIN, which
   is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So,
   COLIN would obtain a score of 938 × 53 = 49714.

   What is the total of all the name scores in the file?


   Visible links
   1. names.txt

Reasoning
---------
   Direct Implementation
"""

__solution__ = "f2c9c91cb025746f781fa4db8be3983f"

def score_names(names):
   def score(name):
      return sum( ord(c)-ord('A')+1 for c in name)
   names = sorted( name.replace(' ','') for name in names )
   scores = [(i+1)*score(name) for i,name in enumerate(names)]
   return sum(scores)

if __name__ == '__main__':
   with open('resources/names.txt','r') as f:
      names = f.read().replace('"','').split(',')
      print(score_names(names))