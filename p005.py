#!/usr/bin/env python

"""
Project Euler Problem 5
=======================

   2520 is the smallest number that can be divided by each of the numbers
   from 1 to 10 without any remainder.

   What is the smallest positive number that is evenly divisible by all of
   the numbers from 1 to 20?

Reasoning
---------
    The GCD will be the product of all the primes to the largest exponent
    that is lower than the number. Thus we take logarithms and multiply the
    prime powers
"""

__solution__ = "bc0d0a22a7a46212135ed0ba77d22f3a"

from numpy import prod
from math import log
from euler.primes import EratosthenesSieve

def minimum_perfect_multiple(n):
    primes = EratosthenesSieve()
    exps = [int(log(n,p)) for p in primes.below(n+1)]
    return prod([ p**e for p,e in zip(primes.below(n+1),exps)])

if __name__ == '__main__':
    assert(minimum_perfect_multiple(10) == 2520)
    print(minimum_perfect_multiple(20))
