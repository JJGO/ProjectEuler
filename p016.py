#!/usr/bin/env python

"""
Project Euler Problem 16
========================

   2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

   What is the sum of the digits of the number 2^1000?

Reasoning
---------
    Just add them, power only takes 10 iterations
"""

__solution__ = "6a5889bb0190d0211a991f47bb19a777"


import numpy as np

def sum_digits(n):
    return sum([int(c) for c in str(n)])

if __name__ == '__main__':

    print(sum_digits(2**1000))
