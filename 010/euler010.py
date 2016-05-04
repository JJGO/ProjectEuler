#!/usr/bin/env python

# Project Euler Problem 10

# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.


# Reasoning:
# Eratosthenes Sieve

import time

def primes_sieve(limit):
    limit = int(limit)
    a = [False] * 2 + [True] * (limit-2)      # Initialize the primality list
    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in range(i*i, limit, i):     # Mark factors non-prime
                a[n] = False

def sum_primes(threshold):
    return sum(primes_sieve(threshold))

if __name__ == '__main__':
    assert(sum_primes(10)==17)
    start = time.time()
    print(sum_primes(2e6))
    print("Done! Took %.6fs" % (time.time()-start))