#!/usr/bin/env python

"""
Project Euler Problem 26
========================

   A unit fraction contains 1 in the numerator. The decimal representation of
   the unit fractions with denominators 2 to 10 are given:

     1/2  =  0.5
     1/3  =  0.(3)
     1/4  =  0.25
     1/5  =  0.2
     1/6  =  0.1(6)
     1/7  =  0.(142857)
     1/8  =  0.125
     1/9  =  0.(1)
     1/10 =  0.1

   Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can
   be seen that 1/7 has a 6-digit recurring cycle.

   Find the value of d < 1000 for which ^1/[d] contains the longest recurring
   cycle in its decimal fraction part.

Reasoning
---------
    Background in cyclic number https://en.wikipedia.org/wiki/Cyclic_number
    
    Iterative approach.
    We only consider primes p that are not factors of the base b
    FOREACH p
        0) cyclic number n=0, remainder r=1, group size t=0
        DO
            1) We multiply r by the base b (we are computing the next item in the decimal representation)
            2) We computer the integer division d and remainder r of dividing by p
            3) Decimal representation is multiplied by the base and gets added the remainder
        UNTIL remainder=1
        IF group size == p-1
            we have a Fermat quotient and we n is a cyclic number.
            If it is longer than the current sequence substitute.

    Improvement: instead of looking at all, since the length of the sequence is p-1 once we have a valid p
    that generates a cyclic number, we are done.

"""

__solution__ = "6aab1270668d8cac7cef2566a1c5f569"

from euler.primes import EratosthenesSieve

def longest_repeating_sequence(threshold,b=10):
    """
    Returns the denominator d such that 1/d produces the longest repeating sequence
    of decimal expansios in base b for 1 < d < threshold
    """
    primes = EratosthenesSieve().below(threshold)
    primes = [ p for p in primes if b % p != 0]
    for p in primes[::-1]:
        t,r,n = 0,1,0
        while(True):
            t += 1
            x = r*b
            d,r = x // p, x % p
            n = n*b+d
            if(r==1):
                break
        if t == p-1:
            return n,p

def main():
    seq, den = longest_repeating_sequence(1000)
    return den

if __name__ == '__main__':
    print(main())