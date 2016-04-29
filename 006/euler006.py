#!/usr/bin/env python

# Project Euler Problem 6

# The sum of the squares of the first ten natural numbers is,
# 12 + 22 + ... + 102 = 385
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)2 = 552 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

# Reasoning:
# (x_1+x_2+...+x_n)**2 = x_1**2 + .. + x_m**2 + 2*x_1*x_2+ .. + 2*x_{n-1}*x_n

import numpy as np
import itertools
import time

def sum_square_difference(n):
    return 2*np.sum([a*b for a,b in itertools.combinations(range(1,n+1),2)])

if __name__ == '__main__':
    assert(sum_square_difference(10)==2640)
    start = time.time()
    print(sum_square_difference(100))
    print("Done! Took %.6fs" % (time.time()-start))