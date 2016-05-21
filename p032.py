#!/usr/bin/env python

"""
Project Euler Problem 32
========================

   We shall say that an n-digit number is pandigital if it makes use of all
   the digits 1 to n exactly once; for example, the 5-digit number, 15234, is
   1 through 5 pandigital.

   The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing
   multiplicand, multiplier, and product is 1 through 9 pandigital.

   Find the sum of all products whose multiplicand/multiplier/product
   identity can be written as a 1 through 9 pandigital.

   HINT: Some products can be obtained in more than one way so be sure to
   only include it once in your sum.

Reasoning
---------
"""

__solution__ = "100f6e37d0b0564490a2ee27eff0660d"

import itertools

def list2num(number):
    return int(''.join(str(i) for i in number))

def pandigital_products():
    digits = set(range(1,10))
    pan_products = set()
    for a,b in [(1,4),(2,3)]:
        for p in itertools.permutations(digits,a):
            for q in itertools.permutations(digits-set(p),b):
                prod = list2num(p)*list2num(q)
                if len(str(prod)) >= 5:
                    continue
                r = {int(i) for i in str(prod)}
                if r == digits-set(q)-set(p):
                    pan_products.add(prod)
    return pan_products

def main():
    return sum(pandigital_products())

if __name__ == '__main__':
    print(main())

