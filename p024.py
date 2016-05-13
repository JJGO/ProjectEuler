#!/usr/bin/env python

"""
Project Euler Problem 24
========================

   A permutation is an ordered arrangement of objects. For example, 3124 is
   one possible permutation of the digits 1, 2, 3 and 4. If all of the
   permutations are listed numerically or alphabetically, we call it
   lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

                       012   021   102   120   201   210

   What is the millionth lexicographic permutation of the digits 0, 1, 2, 3,
   4, 5, 6, 7, 8 and 9?

Reasoning
---------
    Naive approach using generator and lazy evaluation

    Better solution prevents computing the previous permutations and computes
    the *coordinates* of the permutation using division and remainder arithmetic.
    
    choice, position = position / i!, position mod i!

"""

__solution__ = "7f155b45cb3f0a6e518d59ec348bff84"


import itertools as it
from math import factorial

def nth_permutation(elements,n):
    return next(it.islice(it.permutations(elements), n, None), None)

def nth_permutation(elements,n):
    position = n
    permutation = []
    remaining_elements = list(elements)[:]
    for i in reversed(range(len(elements))):
        size_choice = factorial(i)
        choice, position = position // size_choice, position % size_choice
        permutation.append(remaining_elements.pop(choice))
    return permutation
    

if __name__ == '__main__':
    p = nth_permutation(range(10),int(1e6-1))
    print("".join( str(n) for n in p ))