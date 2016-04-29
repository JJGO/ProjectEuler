#!/usr/bin/env python

# Project Euler Problem 3
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

# Note Second method is assymptotically better

import numpy as np
import time

def primes_sieve(limit):
    a = [False] * 2 + [True] * (limit-2)      # Initialize the primality list

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in range(i*i, limit, i):     # Mark factors non-prime
                a[n] = False

def is_prime(num):
    primes = list(primes_sieve(int(num**0.5)+1))
    for p in primes:
        if num % p == 0:
            return False
    else:
        return True

def largest_factor(num):
    sqr = int(num**0.5)
    max_prime = 1
    for i in range(2,sqr+1):
        if num % i == 0:
            d = num / i
            # print(i,d)
            if is_prime(d):
                return d
            elif is_prime(i):
                max_prime = i
    else:
        return max_prime

def largest_factor2(num):
    primes = list(primes_sieve(int(num**0.5)+1))
    for p in primes:
        while num % p == 0:
            if num / p == 1:
                return num
            num /= p
    else:
        return 1

if __name__ == '__main__':
    start = time.time()
    print(largest_factor(600851475143))
    print("Done! Took %.6fs" % (time.time()-start))
    start = time.time()
    print(largest_factor2(600851475143))
    print("Done! Took %.6fs" % (time.time()-start))