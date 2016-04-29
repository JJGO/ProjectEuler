#!/usr/bin/env python

# Project Euler Problem 5

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# Answer: 232792560

from numpy import prod
from math import log
import time

def primes_sieve(limit):
   a = [False] * 2 + [True] * (limit-2)      # Initialize the primality list
   for (i, isprime) in enumerate(a):
       if isprime:
           yield i
           for n in range(i*i, limit, i):     # Mark factors non-prime
               a[n] = False

def minimum_perfect_multiple(n):
    primes = [i  for i in primes_sieve(n+1)]
    exps = [int(log(n,p)) for p in primes]
    return prod([ p**e for p,e in zip(primes,exps)])

if __name__ == '__main__':
    start = time.time()
    print(minimum_perfect_multiple(20))
    print("Done! Took %.6fs" % (time.time()-start))