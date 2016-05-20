#!/usr/bin/env python

"""
Project Euler Problem 23
========================

   A perfect number is a number for which the sum of its proper divisors is
   exactly equal to the number. For example, the sum of the proper divisors
   of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect
   number.

   A number n is called deficient if the sum of its proper divisors is less
   than n and it is called abundant if this sum exceeds n.

   As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the
   smallest number that can be written as the sum of two abundant numbers is
   24. By mathematical analysis, it can be shown that all integers greater
   than 28123 can be written as the sum of two abundant numbers. However,
   this upper limit cannot be reduced any further by analysis even though it
   is known that the greatest number that cannot be expressed as the sum of
   two abundant numbers is less than this limit.

   Find the sum of all the positive integers which cannot be written as the
   sum of two abundant numbers.

Reasoning
---------
   We can create a sieve for the divisors from bottom up, by just adding each number
   to all of its multiples below the absolute limit of 28123. Then we can filter the
   abundant numbers and create a hashset with them. Finally, we can iterate from 1 to limit
   and check for every number if substracting any abundant number returns another abundant
   number.
"""

__solution__ = "2c8258c0604152962f7787571511cf28"

import itertools
from euler.primes import EratosthenesSieve
import numpy as np

def non_abundant_sum_sieve(threshold = 28123):
   sum_proper_divisors = np.zeros(threshold+1)
   for i in range(1,threshold+1):
      sum_proper_divisors[2*i::i] += i
   abundant = set( i for i in range(1,threshold+1) if sum_proper_divisors[i] > i)
   non_abundant = sum( i for i in range(1,threshold+1) if not any( (i-a) in abundant for a in abundant ) )
   return non_abundant

if __name__ == '__main__':
   print(non_abundant_sum_sieve())
