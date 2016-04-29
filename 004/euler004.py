#!/usr/bin/env python

# Project Euler Problem 4
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

# Answer:


import numpy as np
import time
import itertools

def largest_composite_palindrome(n):
    for j in range(n,0,-1):
        for digits in itertools.product(reversed(range(10)),repeat=j):
            r_digits =  digits+digits[::-1]
            palindrome = sum(d*10**i for i,d in enumerate(r_digits))
            for factor in range(10**n-1,10**(n-1)-1,-1):
                if palindrome % factor == 0:
                    factor2 = palindrome/factor
                    if factor2 >= 10**(n-1) and factor2 < 10**n:
                        return palindrome


# def largest_factor2(num):
#     primes = list(primes_sieve(int(num**0.5)+1))
#     for p in primes:
#         while num % p == 0:
#             if num / p == 1:
#                 return num
#             num /= p
#     else:
#         return 1

if __name__ == '__main__':
    start = time.time()
    print(largest_composite_palindrome(3))
    print("Done! Took %.6fs" % (time.time()-start))