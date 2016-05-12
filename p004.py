#!/usr/bin/env python

"""
Project Euler Problem 4
=======================

   A palindromic number reads the same both ways. The largest palindrome made
   from the product of two 2-digit numbers is 9009 = 91 × 99.

   Find the largest palindrome made from the product of two 3-digit numbers.

Reasoning
---------
    There are less palindromes than products of two digits so we just enumerate the palindromes
    in descending order and try to factor them
"""

__solution__ = "d4cfc27d16ea72a96b83d9bdef6ce2ec"

import numpy as np
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

if __name__ == '__main__':
    assert(largest_composite_palindrome(2)==9009)
    print(largest_composite_palindrome(3))

