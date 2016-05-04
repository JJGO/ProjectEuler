#!/usr/bin/env python

# Project Euler Problem 16

#215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

# What is the sum of the digits of the number 21000?



import time
import numpy as np

def sum_digits(n):
    return sum([int(c) for c in str(n)])

if __name__ == '__main__':
    
    start = time.time()
    print(sum_digits(2**1000))
    print("Done! Took %.6fs" % (time.time()-start))