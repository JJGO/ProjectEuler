#!/usr/bin/env python

# Project Euler Problem 14

# The following iterative sequence is defined for the set of positive integers:

# n → n/2 (n is even)
# n → 3n + 1 (n is odd)

# Using the rule above and starting with 13, we generate the following sequence:

# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

# Which starting number, under one million, produces the longest chain?
# NOTE: Once the chain starts the terms are allowed to go above one million.

import time
import numpy as np


def collatz_length(n):
    if n not in collatz_length.cache:
        n_1 = n/2 if n % 2 == 0 else 3*n+1
        collatz_length.cache[n] = 1 + collatz_length(n_1)
    return collatz_length.cache[n]
collatz_length.cache = {1:1}

def longest_collatz_sequence(threshold):
    threshold = int(threshold)
    max_length = 1
    max_index = 1
    for i in range(1,threshold):
        length = collatz_length(i)
        if length > max_length:
            max_length,max_index = length,i
    return max_index

if __name__ == '__main__':
    
    start = time.time()
    print(longest_collatz_sequence(1e6))
    print("Done! Took %.6fs" % (time.time()-start))