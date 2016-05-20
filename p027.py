#!/usr/bin/env python

"""
Project Euler Problem 27
========================

   Euler discovered the remarkable quadratic formula:

                                  n² + n + 41

   It turns out that the formula will produce 40 primes for the consecutive
   values n = 0 to 39. However, when n = 40, 40^2 + 40 + 41 = 40(40 + 1) + 41
   is divisible by 41, and certainly when n = 41, 41² + 41 + 41 is clearly
   divisible by 41.

   The incredible formula  n² − 79n + 1601 was discovered, which produces 80
   primes for the consecutive values n = 0 to 79. The product of the
   coefficients, −79 and 1601, is −126479.

   Considering quadratics of the form:

     n² + an + b, where |a| < 1000 and |b| < 1000

     where |n| is the modulus/absolute value of n
     e.g. |11| = 11 and |−4| = 4

   Find the product of the coefficients, a and b, for the quadratic
   expression that produces the maximum number of primes for consecutive
   values of n, starting with n = 0.

Reasoning
---------
  Since for n = 0 has to be prime we can reduce the values of b to be just
  primes below the threshold.
  
  Since n takes both even and odd values, for n odd we have
  (n=odd)^2 + a(n=odd) + (b=odd) = a(n=odd)+(even) so (a) needs to be odd to
  ensure this combination is odd too, and thus can be prime.

  Finally, we know that n^2+an+b cannot be factored so the equation must give
  complex numbers. Thus a^2-4b < 0. So for a prime b, |a| < 2sqrt(b)

"""

__solution__ = "69d9e3218fd7abb6ff453ea96505183d"

from euler.primes import EratosthenesSieve
import itertools
from math import floor

def longest_quadratic_prime_chain(threshold):
    max_length,max_a,max_b = 0,0,0
    primes = EratosthenesSieve(threshold)
    len_iterable = lambda it: sum(1 for _ in it)

    for b in primes.below(threshold): #0*0+a*0+b need to be prime
        c = floor(b**0.5)*2
        c = c-1 if c % 2 == 0 else c # Needs to be odd
        for a in range(-c,c+1,2): # Only consider odd numbers
            candidate_primes = (n*n+a*n+b for n in itertools.count() )
            l = len_iterable(itertools.takewhile(primes.is_prime, candidate_primes ) )
            if l > max_length:
                max_length,max_a,max_b = l,a,b
    return max_a*max_b

def main():
    return longest_quadratic_prime_chain(1000)

if __name__ == '__main__':
    print(main())

