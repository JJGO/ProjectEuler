#!/usr/bin/env python

"""
Project Euler Problem 10
========================

   The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

   Find the sum of all the primes below two million.

Reasoning
---------
    We use a simple Eratosthenes Sieve
"""

__solution__ = "d915b2a9ac8749a6b837404815f1ae25"

from euler.primes import primes_below

def sum_primes(threshold):
    return sum(primes_below(threshold))

if __name__ == '__main__':
    assert(sum_primes(10)==17)
    print(sum_primes(2e6))
