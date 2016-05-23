#!/usr/bin/env python

"""
Project Euler Problem 35
========================

   The number, 197, is called a circular prime because all rotations of the
   digits: 197, 971, and 719, are themselves prime.

   There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37,
   71, 73, 79, and 97.

   How many circular primes are there below one million?

Reasoning
---------
"""

__solution__ = "b53b3a3d6ab90ce0268229151c9bde11"

import itertools
import numpy as np
from euler.primes import EratosthenesSieve

def list2num(number):
   return int(''.join(str(i) for i in number))

def circular_primes(threshold):
    threshold = int(threshold)
    primes = EratosthenesSieve(threshold)
    prime_digits = [1,3,7,9]
    num_digits = len(str(threshold-1))
    circular_primes = {2,3,5,7}
    for n in range(2,num_digits+1):
        for i,j in enumerate(prime_digits):
            for digits in itertools.product(prime_digits[i:],repeat=n-1):
                digits = (j,) + digits
                p = list2num(digits)
                if p in circular_primes:
                    continue
                elif p > threshold:
                    break
                rotations = {list2num(np.roll(digits,s)) for s in range(n)}
                if all( primes.is_prime(r) for r in rotations ):
                    circular_primes.update(rotations)
    return sorted(circular_primes)

def main():
    return len(circular_primes(1e6))

if __name__ == '__main__':
    assert( circular_primes(100) == [2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97] )
    print(main())

