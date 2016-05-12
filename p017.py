#!/usr/bin/env python

"""
Project Euler Problem 17
========================

   If the numbers 1 to 5 are written out in words: one, two, three, four,
   five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

   If all the numbers from 1 to 1000 (one thousand) inclusive were written
   out in words, how many letters would be used?

   NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
   forty-two) contains 23 letters and 115 (one hundred and fifteen) contains
   20 letters. The use of "and" when writing out numbers is in compliance
   with British usage.

Reasoning
---------
    Use python inflect engine
"""

__solution__ = "6a979d4a9cf85135408529edc8a133d0"

import inflect

if __name__ == '__main__':
    p = inflect.engine()
    letters = sum(len(p.number_to_words(i).replace(' ','').replace('-','')) for i in range(1,1001))
    print(letters)

