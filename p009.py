#!/usr/bin/env python

"""
Project Euler Problem 9
=======================

   A Pythagorean triplet is a set of three natural numbers, a < b < c, for
   which,

                                a^2 + b^2 = c^2

   For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

   There exists exactly one Pythagorean triplet for which a + b + c = 1000.
   Find the product abc.

Reasoning
---------
    All Pitagorean Triples can be expressed as (m**2-n**2,2*m*n,m**2+n**2)
    The sum is thus 2m**2 + 2mn = M -> m*(m+n) = M/2 with m>n
    We can search for m <= sqrt(S/2) and as soon as it divides we have n

"""

__solution__ = "24eaa9820350012ff678de47cb85b639"

import numpy as np
from numpy import prod
from math import ceil

def triplet_from_sum(s):
    M = ceil((s/2)**0.5)-1
    for m in range(M,0,-1):
        if s/2 % m == 0:
            n = s/2/m-m
            return tuple(sorted((m**2-n**2,2*m*n,m**2+n**2)))
    else:
        return None

if __name__ == '__main__':
    assert(triplet_from_sum(12) == (3,4,5))
    print(int(prod(triplet_from_sum(1000))))
