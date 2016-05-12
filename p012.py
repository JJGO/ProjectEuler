#!/usr/bin/env python

"""
Project Euler Problem 12
========================

   The sequence of triangle numbers is generated by adding the natural
   numbers. So the 7^th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 =
   28. The first ten terms would be:

                    1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

   Let us list the factors of the first seven triangle numbers:

      1: 1
      3: 1,3
      6: 1,2,3,6
     10: 1,2,5,10
     15: 1,3,5,15
     21: 1,3,7,21
     28: 1,2,4,7,14,28

   We can see that 28 is the first triangle number to have over five
   divisors.

   What is the value of the first triangle number to have over five hundred
   divisors?

Reasoning
---------
    If we know the prime factorization of a number, then the number of divisors
    is just the product of the successors of the exponents

        x = p_1^e_1 * p_2^e_2 * ... * p_n^e_n
        d(x) = (e_1 + 1) * (e_2 + 1) * ... * (e_n + 1)

    For a triangular number we know t = n*(n+1)/2 so given the prime factorization
    of n and n+1 we can get the factorization for t

    Since we are interested in the first that meets the condition we just increase n
    until d(t) > 500
"""

__solution__ = "8091de7d285989bbfa9a2f9f3bdcc7c0"

from euler.primes import EratosthenesSieve
from collections import defaultdict
import numpy as np

def triangular_number_divisors(min_div):
    E = EratosthenesSieve()
    i,n = 1,1
    G = E.factor(i)
    while (n < min_div):
        F,G = G,E.factor(i+1)
        i += 1
        d = defaultdict(int)
        for p,e in F+G:
            d[p] += e
        d[2] -= 1
        n = np.product([d[p]+1 for p in d])
    return i*(i-1) // 2

if __name__ == '__main__':
    print(triangular_number_divisors(500))


