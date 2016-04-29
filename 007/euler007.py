#!/usr/bin/env python

# Project Euler Problem 7

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?


# Reasoning:
# Eratosthenes Sieve

import numpy as np
from itertools import islice
import time

def nth(iterable, n, default=None):
        "Returns the nth item or a default value"
        return next(islice(iterable, n, None), default)

def primes_sieve(limit):
    limit = int(limit)
    a = [False] * 2 + [True] * (limit-2)      # Initialize the primality list
    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in range(i*i, limit, i):     # Mark factors non-prime
                a[n] = False

def nth_prime(n):
    limit = 10
    prime = None
    while not prime:
        prime = nth(primes_sieve(limit),n-1,None)
        limit *= 10
    return prime

if __name__ == '__main__':
    assert(nth_prime(6)==13)
    start = time.time()
    print(nth_prime(10001))
    print("Done! Took %.6fs" % (time.time()-start))