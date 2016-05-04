#!/usr/bin/env python

# Project Euler Problem 13

# Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.

import time
import numpy as np

def first_digits(number,digits):
    return str(number)[:digits]

if __name__ == '__main__':
    with open('numbers.txt','r') as f:
        numbers = np.array([int(i) for i in f.read().split('\n')])
        start = time.time()
        print(first_digits(np.sum(numbers),10))
        print("Done! Took %.6fs" % (time.time()-start))