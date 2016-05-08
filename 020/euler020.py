#!/usr/bin/env python

# Project Euler Problem 20

# n! means n × (n − 1) × ... × 3 × 2 × 1

# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

# Find the sum of the digits in the number 100!
import time
from math import factorial


if __name__ == '__main__':
    start = time.time()
    digit_sum = sum([int(n) for n in str(factorial(100))])
    print(digit_sum)
    print("Done! Took %.6fs" % (time.time()-start))