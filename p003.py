#!/usr/bin/env python

"""
Project Euler Problem 3
=======================

   The prime factors of 13195 are 5, 7, 13 and 29.

   What is the largest prime factor of the number 600851475143 ?

Reasoning
---------
    Just factor the number and get the biggest prime factor
"""

__solution__ = "94c4dd41f9dddce696557d3717d98d82"

import numpy as np
from euler.primes import EratosthenesSieve

def largest_factor(num):
    primes = EratosthenesSieve(num,sqrt_thr=True)
    factors = primes.factor(num)
    p,e = factors[-1]
    return p

if __name__ == '__main__':
    print(largest_factor(600851475143))

