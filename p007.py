#!/usr/bin/env python

"""
Project Euler Problem 7
=======================

   By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
   that the 6th prime is 13.

   What is the 10 001st prime number?

Reasoning
---------
  We use a simple Eratosthenes Sieve
"""

__solution__ = "8c32ab09ec0210af60d392e9b2009560"


import numpy as np
from itertools import islice
from euler.primes import primes_below

def nth(iterable, n, default=None):
        "Returns the nth item or a default value"
        return next(islice(iterable, n, None), default)

def nth_prime(n):
    limit = 10
    prime = None
    while not prime:
        prime = nth(primes_below(limit),n-1,None)
        limit *= 10
    return prime

if __name__ == '__main__':
    assert(nth_prime(6)==13)
    print(nth_prime(10001))
